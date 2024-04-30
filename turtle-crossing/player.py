from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        #self.create_player()

    def create_player(self):
        player = Turtle("turtle")
        player.goto(x=0, y=-280)
        player.left(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def left(self):
        pass
        #self.left(MOVE_DISTANCE)
    def right(self):
        pass
        #self.right(MOVE_DISTANCE)