import random

from game_exceptions import EnemyDown


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown()

