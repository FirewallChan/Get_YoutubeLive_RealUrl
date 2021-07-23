import requests
import subprocess


proxy ={"https":"http://127.0.0.1:10809"}

class Youtube:

    
    def __init__(self,Channel_ID):
        self.Channel_ID = Channel_ID
        self.C_url = "https://www.youtube.com/channel/{}/live".format(Channel_ID)

    def get_youtube_live_status(self):
        res = requests.get(self.C_url,proxies=proxy)
        if res.status_code == 200:
            return True
        else:
            return False

    def get_youtube_live_url(self):
        cmd = "youtube-dl -f best -g --proxy 127.0.0.1:10809 \""+self.C_url+"\""
        res = subprocess.run(cmd,encoding="utf-8",stdout=subprocess.PIPE)
        return res.stdout

def getUrl(Channel_ID):
    channel = Youtube(Channel_ID=Channel_ID)
    if channel.get_youtube_live_status():
        return channel.get_youtube_live_url()
    else:
        return 0