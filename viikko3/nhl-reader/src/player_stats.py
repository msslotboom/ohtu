from player import Player

class PlayerStats:
    def __init__(self, reader) -> None:
        self.players = []
        for player in reader.players:
            self.players.append(player)

    def top_scorers_by_nationality(self, nationality):
        return list(filter(lambda player: player.nationality == nationality, self.players))
    