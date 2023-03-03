class GameOver(Exception):
    def __init__(self, score):
        self.score = score

    def save_score(self):
        with open("scores.txt", "a") as f:
            f.write(f"{self.score}/n")


class EnemyDown(Exception):
    pass
