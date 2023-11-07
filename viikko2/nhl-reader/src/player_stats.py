from player import Player

class PlayerStats:
    def __init__(self,reader):
        self.players = []
        for player_dict in reader.response:
            player = Player(player_dict)
            self.players.append(player)

    def top_scorers_by_nationality(self, nationality):
        players_from_nationality = filter(lambda n: n.nationality == nationality,self.players)
        return sorted(players_from_nationality,reverse=True,key=sort_by_points)

def sort_by_points(player):
    return player.points