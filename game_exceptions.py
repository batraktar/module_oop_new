class GameOver(Exception):
    def __init__(self, score, name):
        self.score = score
        self.name = name

    def save_score(self):
        with open("scores.txt", "a") as f:
            f.write(f"{self.name}: {self.score}/n")


class EnemyDown(Exception):
    pass
