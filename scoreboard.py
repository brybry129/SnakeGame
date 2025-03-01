from turtle import Turtle


POSITION = (0, 270)
COLOR = "white"
FONT = ('Arial', 20, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.goto(POSITION)
        self.high_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=FONT)
        if self.score > self.high_score :
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{str(self.high_score)}")

