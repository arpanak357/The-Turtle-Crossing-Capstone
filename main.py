import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()   # since player is created in constructor only creating obj does work
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)   # to refresh screen every 0.1 sec
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    #detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # detecting successful crossing
    if player.is_at_finish():
        player.goto_start()
        car_manager.level_up()
        score.increase_level()



screen.exitonclick()
