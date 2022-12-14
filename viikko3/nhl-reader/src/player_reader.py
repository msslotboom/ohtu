import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

        response = requests.get(url).json()
        self.players = []

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['nationality'],
                player_dict['goals'],
                player_dict['assists']
            )
            self.players.append(player)
