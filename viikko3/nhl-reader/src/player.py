class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
    
    def __str__(self):
        return '{} team {} goals {} assists {} '.format(self.name, self.team, self.goals, self.assists)
