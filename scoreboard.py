from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score_counter()

    def score_counter(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Courier', 18, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as new_data:
                new_data.write(f"{self.high_score}")
            self.score = 0
            self.score_counter()

    def increase_score(self):
        self.score += 1
        self.score_counter()



