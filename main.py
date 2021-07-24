import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
timmy = Player()
score = Scoreboard()
screen.listen()
screen.onkey(timmy.move_fd, 'Up')
cars = CarManager()
cars.create_cars()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    for call_detect in cars.show_room:
        if call_detect.distance(timmy) < 15 or call_detect.distance(timmy) < 20:
            score.lost()
            game_is_on = False

    if timmy.ycor() >= FINISH_LINE_Y:
        score.level_up()
        cars.car_speed_up()
        timmy.reset_positions()

screen.exitonclick()
