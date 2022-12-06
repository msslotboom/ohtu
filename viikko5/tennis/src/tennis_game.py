class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points = self.player1_points + 1
        else:
            self.player2_points = self.player2_points + 1

    def _point_to_text(self, point):
        if point == 0:
            return "Love"
        if point == 1:
            return "Fifteen"
        if point == 2:
            return "Thirty"
        if point == 3:
            return "Forty"
        
    def _get_score_if_equal(self):
        if self.player1_points >= 4:
                return "Deuce"
        else:
           return self._point_to_text(self.player1_points) + "-All"

    def _get_score_above_four(self):
        point_difference = self.player1_points - self. player2_points

        if point_difference == 1:
            score = "Advantage player1"
        elif point_difference == -1:
            score = "Advantage player2"
        elif point_difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def _get_score_if_not_equal_but_under_four(self):
        score = ""
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_points
            else:
                score = score + "-"
                temp_score = self.player2_points

            score = score + self._point_to_text(temp_score)
        return score
        
    def get_score(self):
        score = ""

        if self.player1_points == self.player2_points:
            score = self._get_score_if_equal()

        elif self.player1_points >= 4 or self.player2_points >= 4:
            score = self._get_score_above_four()
        else:
            score = self._get_score_if_not_equal_but_under_four()

        return score
