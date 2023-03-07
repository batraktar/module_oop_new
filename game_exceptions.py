""" Contains special exceptions that control gameplay"""


class GameOver(Exception):
    """ The end of the game and recording the score """
    def __init__(self, score, name, mode):
        """ Creating attribute score """
        self.score = score
        self.name = name
        self.mode = mode

    def save_score(self):
        """ Implemented method to save the final score """
        with open("scores.txt", "a+", encoding="utf8") as file:
            file.write(f'NAME: {self.name}| SCORE: {self.score}| MODE: {self.mode}\n')


class EnemyDown(Exception):
    """ Defeat the enemy """


class ExitGame(Exception):
    """ Exit Game """
