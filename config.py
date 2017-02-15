import yaml
import sys

import random
import string

class Config():
    def __init__(self, fileName):

        global cfg

        try:
            with open(fileName, 'r') as ymlfile:
                cfg = yaml.load(ymlfile)
        except Exception as e:
            print(e)
            input("Press any key to exit the program")
            sys.exit()

        if not cfg['config']['connection']['Google api key'] and not cfg['config']['connection']['Discord bot token']:
            input('Problem loading Google api key/Discord bot token. Make sure filled the fields')
            sys.exit()

        if self.getYouTubersNr() == 0:
            input('No YouTubers in list')
            sys.exit()

    def getConnectionData(self):
        return [cfg['config']['connection']['Google api key'], cfg['config']['connection']['Discord bot token']]

    def getPingTime(self):
        return cfg['config']['main']['Ping Every x Minutes']

    def getYouTubersList(self):
        return cfg['config']['YouTubers']

    def getYouTubersNr(self):
        if not cfg['config']['YouTubers']:
            return 0
        return len(cfg['config']['YouTubers'])
