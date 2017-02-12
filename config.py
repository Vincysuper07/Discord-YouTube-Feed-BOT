import yaml

class Config():
    cfg = ''
    def __init__(self):
        try:
            print("Importing config.yml")
            with open("config.yml", 'r') as ymlfile:
                self.cfg = yaml.load(ymlfile)
        except Exception as e:
            print(e)
            input("Press any key to exit the program")
            exit

        if self.cfg['config']['connection']['Google api key'] == 'None' and self.cfg['config']['connection']['Discord bot token'] == 'None':
            input('Problem loading Google api key/Discord bot token. Make sure filled the fields')
            exit

        if len(self.cfg['config']['YouTubers']) == 0:
            input('There are no youtubers in your list.')
            exit

        print("config.yml imported succesfully")

    def getConnectionData(self):
        return [self.cfg['config']['connection']['Google api key'], self.cfg['config']['connection']['Discord bot token']]

    def getPingTime(self):
        return self.cfg['config']['main']['Ping Every x Minutes']

config = Config()

print(config.getConnectionData())