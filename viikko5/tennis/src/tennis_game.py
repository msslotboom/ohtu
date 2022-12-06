class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

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
        if self.m_score1 >= 4:
                return "Deuce"
        else:
           return self._point_to_text(self.m_score1) + "-All"

    def _get_score_above_four(self):
        minus_result = self.m_score1 - self. m_score2

        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def _get_score_if_not_equal_under_four(self):
        score = ""
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.m_score1
            else:
                score = score + "-"
                temp_score = self.m_score2

            score = score + self._point_to_text(temp_score)
        return score
        
    def get_score(self):
        score = ""

        if self.m_score1 == self.m_score2:
            score = self._get_score_if_equal()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self._get_score_above_four()
        else:
            score = self._get_score_if_not_equal_under_four()

        return score
