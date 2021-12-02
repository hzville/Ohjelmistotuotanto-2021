class TennisGame:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def won_point(self, player):
        player.add_point()
    
    def get_score(self):

        if self.player1.get_score() == self.player2.get_score():
            return self.game_score_even(self.player1.get_score())

        elif self.player1.get_score() >= 4 or self.player2.get_score() >= 4:
            minus_result = self.player1.get_score() - self.player2.get_score()
            return self.enter_final(minus_result)

        else:
            return self.enter_pre_final(self.player1, self.player2)
    
    def game_score_even(self, score):
        if score == 0:
            return "Love-All"
        elif score == 1:
            return "Fifteen-All"
        elif score == 2:
            return "Thirty-All"
        elif score == 3:
            return "Forty-All"
        else:
            return "Deuce"
    
    def enter_final(self, minus_result):
            if minus_result == 1:
                return "Advantage player1"
            elif minus_result == -1:
                return "Advantage player2"
            elif minus_result >= 2:
                return "Win for player1"
            else:
                return "Win for player2"

    def enter_pre_final(self, player1, player2):
        score = ""
        temp_score = 0

        for i in range(1, 3):
                if i == 1:
                    temp_score = player1.get_score()
                else:
                    score = score + "-"
                    temp_score = player2.get_score()

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"
        return score


