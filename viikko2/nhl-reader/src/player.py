class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = dict['assists']+dict['goals']
    
    def __str__(self):
        return f"{self.name:22}{self.team:4}{self.goals:3} +{self.assists:3} = {self.goals+self.assists}"