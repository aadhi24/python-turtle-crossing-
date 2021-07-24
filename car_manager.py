from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.show_room = []
        self.speed_of_car = STARTING_MOVE_DISTANCE

    def create_cars(self):
        ram = random.randint(1, 5)
        if ram == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.penup()
            new_car.goto(300, random.randint(-150, 250))
            self.show_room.append(new_car)

    def move_cars(self):
        for car_all in self.show_room:
            car_all.forward(self.speed_of_car)

    def car_speed_up(self):
        self.speed_of_car += MOVE_INCREMENT