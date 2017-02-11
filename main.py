import discord
import time
import asyncio
from Api_Test import Youtuber

YoutubeName = 'youtuber name'
GOOGLE_API = 'google api key'
pingEveryXMinutes = 1 # Minutes to wait until next ping. Under 1 min NOT RECOMMENDED.

print('{} >> Collecting Data for {} '.format(time.strftime("%H:%M:%S"), YoutubeName))
api = Youtuber(GOOGLE_API, YoutubeName, False)
liveId = ''

print('{} >> YouTube Data collected succesfully.'.format(time.strftime("%H:%M:%S")))
print('{} >> Starting bot.'.format(time.strftime("%H:%M:%S")))

client = discord.Client()

async def update():
    while True:
        data = api.update()
        print('{} >> {}'.format(time.strftime("%H:%M:%S"), data))
        if api.isNewVideo():
            await client.send_message(client.get_channel('273549788283142166'), '{} just posted a new video!'.format(YoutubeName))
            await client.send_message(client.get_channel('273549788283142166'), '{}'.format(api.getVideoLink(api.videosData[0][1])))

        if api.isUserLive():
            if not api.liveId == liveId:
                await client.send_message(client.get_channel('273549788283142166'), '{} is live!'.format(YoutubeName))
                await client.send_message(client.get_channel('273549788283142166'), '{}'.format(api.getVideoLink(api.getUserLiveData())))

        await asyncio.sleep(pingEveryXMinutes * 60)

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('---------------------------------------')
    await client.send_message(client.get_channel('273549788283142166'), 'YouTube Feed BOT >> Now showing all live video uploads from {}.'.format(YoutubeName))
    asyncio.ensure_future(update())

client.run('discord bot token')
