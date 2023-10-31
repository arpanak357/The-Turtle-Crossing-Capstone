# for the TURTLE which will be crossing the road
#  A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.

# When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.
# When the turtle collides with a car, it's game over and everything stops.

#Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)

    # def create_turtle(self):
    #     tim = Turtle(shape="turtle")
    #     tim.penup()
    #     tim.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

