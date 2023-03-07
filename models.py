import random
from settings import PLAYER_LIVES, ALLOWED_ATTACKS
from game_exceptions import EnemyDown, GameOver


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """ choice to attack the enemy """
        return 1

    def decrease_lives(self):
        """ enemy lives """
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player:
    def __init__(self, name, gmode):
        self.name = name
        self.gmode = gmode
        self.score = 0
        self.lives = PLAYER_LIVES
        self.allowed_attacks = ALLOWED_ATTACKS

    @staticmethod
    def fight(attack, defence):
        """ method w"""
        if attack == defence:
            return 0
        if attack == 1 and defence == 2:
            return 1
        if attack == 2 and defence == 3:
            return 1
        if attack == 3 and defence == 1:
            return 1
        return -1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver(self.score, self.name, self.gmode)
        print(f'Your lives: {self.lives}')

    def attack(self, enemy_obj, mode):
        """ choose player """
        while True:
            try:
                attack = int(input(f"{self.name}, choose your attack(1, 2, 3):\n"))
                if attack not in ALLOWED_ATTACKS:
                    raise ValueError("Invalid attack choice.")
                break
            except ValueError:
                print(f"Invalid input.")
        defence = enemy_obj.select_attack()
        result = self.fight(attack, defence)
        if result == 0:
            print("It's draw!")
        elif result == 1:
            print("You attacked successfully!")
            self.score += (1 * mode)
            print(f'Your score: {self.score}')
            enemy_obj.decrease_lives()
        elif result == -1:
            print("You missed!")
            
    def defence(self, enemy_obj):
        while True:
            try:
                defence = int(input(f"{self.name}, choose your defence(1, 2, 3):\n"))
                if defence not in ALLOWED_ATTACKS:
                    raise ValueError("Invalid defence choice. Please enter a number from 1-3.")
                break
            except ValueError:
                print(f"Invalid input.")
        attack = enemy_obj.select_attack()
        result = self.fight(attack, defence)
        if result == 0:
            print("It's draw!")
        elif result == 1:
            print("You defence worked!")
        elif result == -1:
            print(f"Enemy attack was successfully! Your lives: {self.lives}")
            self.decrease_lives()
