class Player:
    def __init__(self, name, team, goals, assists, total):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.total = total
    
    def __str__(self):
        return '{} team {} {} + {} = {} '.format(self.name, self.team, self.goals, self.assists, self.total)
