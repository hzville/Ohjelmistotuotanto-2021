class Player:
    
    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_score(self):
        return self.score

    def add_point(self):
        self.score += 1