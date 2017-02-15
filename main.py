import discord
import time
import asyncio
import sys
from Api_Test import Youtuber
from config import Config

config = Config('config.yml')

youtubers = config.getYouTubersList() if (config.getYouTubersNr() != 0) else sys.exit()
GOOGLE_API = config.getConnectionData()[0]
pingEveryXMinutes = config.getPingTime()
threads = []
processes = []

i = 0
while i < config.getYouTubersNr():
    temp_list = []
    temp_list.append(config.getYouTubersList()[i]['name'])
    temp_list.append(config.getYouTubersList()[i]['id']) if not config.getYouTubersList()[i]['channelID'] else temp_list.append(config.getYouTubersList()[i]['channelID'])
    temp_list.append(True) if not config.getYouTubersList()[i]['id'] else temp_list.append(False)
    threads.append(temp_list)
    i += 1

print(threads)
pewds = Youtuber(GOOGLE_API, threads[0][1], False)
print(config.getYouTubersNr())

i = 0
while i < 3:
    processes.append(Youtuber(GOOGLE_API, threads[i][1], threads[i][2]))
    i += 1

print(processes)
#liveId = ''

client = discord.Client()

async def update():
    while True:
        item = 0
        while item < 3:
            data = processes[item].update()
            print('{} >> {}'.format(time.strftime("%H:%M:%S"), data))
            if processes[item].isNewVideo():
                await client.send_message(client.get_channel('273549788283142166'), '{} just posted a new video!'.format(threads[item][0]))
                await client.send_message(client.get_channel('273549788283142166'), '{}'.format(processes[item].getVideoLink(processes[item].videosData[0][1])))
            item += 1

        #if api.isUserLive():
        #    if not api.liveId == liveId:
        #        await client.send_message(client.get_channel('273549788283142166'), '{} is live!'.format(YoutubeName))
        #        await client.send_message(client.get_channel('273549788283142166'), '{}'.format(api.getVideoLink(api.getUserLiveData())))

        await asyncio.sleep(pingEveryXMinutes * 60)

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('---------------------------------------')
    await client.send_message(client.get_channel('273549788283142166'),'Now live updates for the following youtubers: {}'.format(threads))
    asyncio.ensure_future(update())

client.run(config.getConnectionData()[1])