from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.create_car()

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 5:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def create_snake(self):
        pass

    def move(self):
        pass
        #car = CarManager()
        #car.forward(STARTING_MOVE_DISTANCE)
        #for seg_num in range():
        #    new_x += STARTING_MOVE_DISTANCE
        #    new_y = y_position
        #    self.segments[seg_num].goto(new_x, new_y)
        #new_car.forward(STARTING_MOVE_DISTANCE)


