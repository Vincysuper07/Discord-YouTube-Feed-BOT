# Discord BOT YouTube Feed

A small Discord BOT that displays live video updates of a YouTube channel, along with a small integration of the YouTube Data V3 API.

### Requirements
- Python 3.5
- Windows OS (only ATM)
- [Discord.py](https://github.com/Rapptz/discord.py)
- Google API Key (with YouTube Data API v3 activated) (Tutorial [here](https://developers.google.com/youtube/v3/getting-started))
- Discord BOT (Tutorial [here](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token))

### Installation
Install the [Discord.py](https://github.com/Rapptz/discord.py) library.
```
python3.5 -m pip install -U discord.py
```
Run the program
```
python3.5 main.py
```
  
If using linux install pyyaml using:
```
python3.5 pip install pyyaml
```
A BETTER INSTALLATION GUIDE COMING SOON

### Features
- Multi Youtuber support
- Config file (config.yml)
- Live YouTube Video Updates
- Livestream updates

### To-Do List
- Better Interface
- BOT Commands
- Personalized YouTube Feed lists (PM video updates)
- Exception Handling

### Changelog
`17/02/2017 ! ` exception handling in case of socket error
`17/02/2017 + ` added linux support   
`16/02/2017 ! ` fixed livestream support  
`15/02/2017 + ` Multi YouTuber Support  
`15/02/2017 + ` Configurable file
