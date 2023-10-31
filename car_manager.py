# for the moving CARS
# Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
class CarManager:

    def __init__(self):
       self.all_cars = []
       self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):                 # creating cars of size 20X40
        rand_chance = random.randint(1,6)
        if rand_chance == 1:
            new_car = Turtle("square")     # no rect shape available
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-240, 250)
            new_car.goto(300, rand_y)   #movement along x-axis
            self.all_cars.append(new_car)

    def move_cars(self):      # moving cars
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

