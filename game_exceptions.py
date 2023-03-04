""" Contains special exceptions that control gameplay"""


class GameOver(Exception):
    """ The end of the game and recording the score """
    def __init__(self, score):
        """Creating attribute score"""
        self.score = score

    def save_score(self):
        """ Implemented method to save the final score """
        with open("scores.txt", "a", encoding="utf8") as file:
            file.write(self.score)


class EnemyDown(Exception):
    """ Defeat the enemy """
