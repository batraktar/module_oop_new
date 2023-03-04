import random
from settings import PLAYER_LIVES
from game_exceptions import EnemyDown, GameOver


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """ choice to attack the enemy """
        return random.randint(1, 3)

    def decrease_lives(self):
        """ enemy lives """
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
        """ method w"""
        if attack == defence:
            return 0
        if (attack == 1 and defence == 2) or\
                (attack == 2 and defence == 3) or\
                (attack == 3 and defence == 1):
            return 1
        return -1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            return GameOver("")

    def attack(self, enemy_obj):
        """ choose player """
        while True:
            try:
                attack = int(input(f"{self.name}, choose your attack(1, 2, 3):\n"))
                if attack not in self.allowed_attacks:
                    raise ValueError("Invalid attack choice.")
                break
            except ValueError as enemy:
                print(f"Invalid input. {enemy}")
        defence = enemy_obj.select_attack()
        result = Player.fight(attack, defence)
        if result == 0:
            print("It's draw!")
        elif result == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
            self.score += 1
        elif result == -1:
            print("You missed!")
            
    def defence(self, enemy_obj):
        while True:
            try:
                defence = int(input(f"{self.name}, choose your defence(1, 2, 3):\n"))
                if defence not in self.allowed_attacks:
                    raise ValueError("Invalid defence choice.")
                break
            except ValueError as enemy:
                print(f"Invalid input. {enemy}")
        attack = enemy_obj.select_attack()
        result = Player.fight(attack, defence)
        if result == 0:
            print("It's draw!")
        elif result == 1:
            print("You defence worked!")
        else:
            print("Enemy attack was successfully!")
            self.decrease_lives()
