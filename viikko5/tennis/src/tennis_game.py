class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1._won_point()
        else:
            self.player2._won_point()
    
    def get_score(self):
        if self.player1.score == self.player2.score:
            score = self._even_score()

        elif self.player1.score >= 4 or self.player2.score >= 4:
            score = self._end_game()

        else:
            score = self._not_even_or_advantage_score()

        return score

    def _even_score(self):
        if self.player1.score == 0:
            return "Love-All"
        elif self.player1.score == 1:
            return "Fifteen-All"
        elif self.player1.score == 2:
            return "Thirty-All"
        else:
            return "Deuce"
    
    def _end_game(self):
        score_difference = self.player1.score - self.player2.score
        leading_player = self.player1.name if score_difference > 0 else self.player2.name
        if abs(score_difference) == 1:
            return "Advantage " + leading_player
        else:
            return "Win for " + leading_player
    
    def _not_even_or_advantage_score(self):
        scores = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        return scores[self.player1.score] + "-" + scores[self.player2.score]
    
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def _won_point(self):
        self.score += 1