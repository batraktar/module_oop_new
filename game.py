""" for the code to work """
import sys
import settings
import models
from game_exceptions import GameOver, EnemyDown, ExitGame


def menu():
    """
    menu game
    """
    print(settings.MENU)


def game_mode():
    """
    input game mode
    returned in lowercase
    """
    while True:
        mode = input('Enter game mode: HARD(H) or NORMAL(N)?\n').strip()
        if mode.lower() in ('normal', 'hard', 'HARD', 'NORMAL', 'H', 'N'):
            return mode.lower()
        print('Invalid game mode. Please, enter "HARD" or "NORMAL".\n')


def show_scores():
    """
    Reads and displays score
    """
    with open('scores.txt', 'r', encoding='utf8') as scf:
        print(scf.read())


def game_exit():
    """
    ExitGame exception
    """
    print('Exit game............')
    sys.exit()


def play():
    """ playing game """
    print("Welcome to game!\nInput START for start game of HELP for show menu: ")
    while True:
        try:
            com = input('Enter your choice:\n')
            if com.lower() == 'exit':
                game_exit()
            elif com.lower() == 'show scores':
                show_scores()
            elif com.lower() == 'start':
                break
            elif com.lower() == 'help':
                menu()
            elif com not in settings.MENU:
                print('Invalid command.')
            else:
                return com
        except ExitGame:
            pass

    name = input("Enter your name: ")

    if game_mode() == "hard":
        gmode = 'hard'
        lives_enemy = settings.HARD
        score_enemy = settings.HARD
    else:
        gmode = 'normal'
        lives_enemy = 1
        score_enemy = 1

    player = models.Player(name, gmode)
    level = 1
    print(f"Level {level}")
    enemy = models.Enemy(lives_enemy)
    print(f' Your level: {level}. Your lives: {player.lives}. Enemy lives: {lives_enemy}.')

    while True:
        try:
            player.attack(enemy, score_enemy)
            player.defence(enemy)
        except EnemyDown:
            player.score += (3 * score_enemy)
            level += 1
            print("You defeated the enemy!")
        enemy = models.Enemy(level)


if __name__ == '__main__':
    try:
        play()
    except GameOver as e:
        e.save_score()
        print(f"Game over. Your final score is {e.score}")
    except KeyboardInterrupt:
        pass
    finally:
        print("Good Bye")
