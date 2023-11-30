class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.scores = {player1_name:0,player2_name:0}
        self.player1_name = player1_name
        self.player2_name = player2_name

    def won_point(self, player_name):
        self.scores[player_name] += 1
    
    def get_score(self):
        if self.scores[self.player1_name] == self.scores[self.player2_name]:
            print((self.scores[self.player1_name], self.scores[self.player2_name]))
            score = self._even_score()

        elif self.scores[self.player1_name] >= 4 or self.scores[self.player2_name] >= 4:
            score = self._end_game()

        else:
            score = self._not_even_or_advantage_score()

        return score

    def _even_score(self):
        if self.scores[self.player1_name] == 0:
            return "Love-All"
        elif self.scores[self.player1_name] == 1:
            return "Fifteen-All"
        elif self.scores[self.player1_name] == 2:
            return "Thirty-All"
        else:
            return "Deuce"
    
    def _end_game(self):
        score_difference = self.scores[self.player1_name] - self.scores[self.player2_name]
        leading_player = self.player1_name if score_difference > 0 else self.player2_name
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
        return scores[self.scores[self.player1_name]] + "-" + scores[self.scores[self.player2_name]]