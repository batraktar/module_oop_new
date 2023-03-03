import random
from settings import PLAYER_LIVES
from game_exceptions import EnemyDown, GameOver


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


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lives = PLAYER_LIVES
        self.allowed_attacks = [1, 2, 3]

    @staticmethod
    def fight(attack, defence):
        if attack == defence:
            return 0
        elif (attack == 1 and defence == 2) or (attack == 2 and defence == 3) or (attack == 3 and defence == 1):
            return 1
        else:
            return -1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            return GameOver("Game Over: You lost all your lives. ")

    def attack(self, enemy_obj):
        attack = int(input("Choose your attack(1, 2, 3):\n"))
        enemy_defence = enemy_obj.select_attack()
        result = Player.fight(attack, enemy_defence)
        if result == 0:
            print("It's draw!")
        elif result == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
            self.score += 1
        elif result == -1:
            print("You missed!")
            
    def defence(self, enemy_obj):
        enemy_attack = enemy_obj.select_attack()
        defence = int(input("Choose your defence(1, 2, 3):\n"))
        result = Player.fight(enemy_attack, defence)
        if result == 0:
            print("It's draw!")
        elif result == 1:
            print("You defence worked!")
        else:
            print("Enemy attack was successfully!")
            self.decrease_lives()
