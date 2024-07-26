import time
import turtle as t
from turtle_movement import Object
from crossing_scoreboard import ScoreBoard
from crossing_cars import Car

# Setting up the screen.
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

update_count = 0
# Beautifying the screen.
# line = t.Turtle()
# line.color("white")
# line.hideturtle()
# line.pensize(5)
# line.setheading(180)
# line.penup()
# x = 300
# y = -270
# line.goto(x, y)
#
# for i in range(0, 600):
#     line.pendown()
#     line.forward(300)
#     line.penup()
#     line.goto(x-100, y-100)
''''''

moving_cars = Car()

# Creating the turtle.
moving_turtle = Object()

# Creating the scoreboard
scoreboard = ScoreBoard()

# Activating the screen to listen for keyboard clicks.
screen.listen()
screen.onkey(key="Up", fun=moving_turtle.up)
screen.onkey(key="w", fun=moving_turtle.up)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    update_count += 1

    # This worked very well but increasing the speed reduced the rate of creation of cars.
    """Adding a new car to the screen after the screen updates 6 times at the beginning"""
    count = 6
    if update_count % count == 0:
        moving_cars.create_car()
    moving_cars.move()

    # Made adjustments on line 13 & 14 of the class crossing cars for better functionality.
    # moving_cars.create_car()
    # moving_cars.move()

    """Increasing the rate of creation of the cars when the user enters a level that is multiple of 3"""
    if scoreboard.count % 2 == 0 and count > 2:
        count -= 2

    # Ending the game once the turtle collides with a car.
    for car in moving_cars.car_storage:
        if moving_turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Condition to check when turtle reaches edge of the screen.
    if moving_turtle.ycor() > 290:
        moving_turtle.setposition(0, -280)
        scoreboard.score_increase()

        # Increasing the speed of the car as turtle progresses through levels.
        moving_cars.increase_speed()

screen.exitonclick()
