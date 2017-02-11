import discord
import time
import asyncio
from Api_Test import YoutubeAPI

YoutubeName = 'name'
GOOGLE_API = 'your google api'

print('Collecting Data for: {}'.format(YoutubeName))
api = YoutubeAPI(GOOGLE_API, YoutubeName)

print('YouTube Data collected succesfully.')
print('Starting bot.')

client = discord.Client()

async def update():
    while True:
        data = api.update()
        print('{} >> {}'.format(time.strftime("%H:%M:%S"), data))
        if api.isNewVideo():
            await client.send_message(client.get_channel('273549788283142166'), '{} just posted a new video!'.format(YoutubeName))
            await client.send_message(client.get_channel('273549788283142166'), '{}'.format(api.getVideoLink(api.videosData[0][1])))

        await asyncio.sleep(2 * 60)

@client.event
async def on_ready():
    print(time.strftime("%H:%M:%S"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--<><><><><>--')
    await client.send_message(client.get_channel('273549788283142166'), 'YouTube Feed BOT >> Now showing all live video uploads from {}.'.format(YoutubeName))
    asyncio.ensure_future(update())

client.run('token')
