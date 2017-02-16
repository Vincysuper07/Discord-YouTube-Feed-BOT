import discord
import time
import asyncio
import sys
from Api_Test import Youtuber
from config import Config

config = Config('config.yml')
client = discord.Client()

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
    temp_list.append('')
    threads.append(temp_list)
    i += 1

i = 0
while i < config.getYouTubersNr():
    processes.append(Youtuber(GOOGLE_API, threads[i][1], threads[i][2]))
    i += 1

async def update():
    while True:
        item = 0
        while item < config.getYouTubersNr():
            data = processes[item].update()
            print('{} >> {}'.format(time.strftime("%H:%M:%S"), data))
            if processes[item].isNewVideo():
                await client.send_message(client.get_channel('273549788283142166'), '{} just posted a new video!'.format(threads[item][0]))
                await client.send_message(client.get_channel('273549788283142166'), '{}'.format(processes[item].getVideoLink(processes[item].videosData[0][1])))


            if processes[item].isUserLive():
                if not processes[item].liveId == threads[item][3]:
                    await client.send_message(client.get_channel('273549788283142166'), '{} is live!'.format(threads[item][0]))
                    await client.send_message(client.get_channel('273549788283142166'), '{}'.format(processes[item].getVideoLink(processes[item].getUserLiveData())))
            item += 1
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