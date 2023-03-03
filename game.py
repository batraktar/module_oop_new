from models import Player, Enemy
from game_exceptions import GameOver, EnemyDown


def play():
    name = input("Enter your name: ")
    player = Player(name)
    level = 1
    while True:
        try:
            print(f"Level {level}")
            enemy = Enemy(level)
            while True:
                player.attack(enemy)
                player.defence(enemy)
        except EnemyDown:
            print("You defeated the enemy!")
            level += 1
        except GameOver as e:
            print(f"Game over: Your final score is {e.score}")
            break


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        pass
    finally:
        print("Good Bye")

