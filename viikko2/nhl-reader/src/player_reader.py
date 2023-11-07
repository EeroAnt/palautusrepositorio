import requests

class PlayerReader:
    def __init__(self, url):
        self.response = self.get_players(url)

    def get_players(self,url):
        return requests.get(url).json()
