from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:

    def __init__(self):
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=280)
