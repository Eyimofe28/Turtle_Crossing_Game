import random
import turtle as t


class Car:
    def __init__(self):
        self.car_storage = []
        self.distance = 6
        self.current_speed = 4

    def create_car(self):
        # Setting up Car qualities.
        # random_number = random.randint(1, 6)
        # if random_number == 1:
        new_car = t.Turtle()
        car_colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
                      "white", "gray", "cyan", "magenta", "lime", "turquoise"]
        new_car.turtlesize(stretch_len=2.5)
        new_car.setheading(180)
        color = random.choice(car_colors)
        new_car.color(color)
        new_car.speed(self.current_speed)
        new_car.shape("square")
        new_car.penup()
        y_axis = random.randint(-250, 250)
        new_car.setposition(300, y_axis)
        self.car_storage.append(new_car)

    def move(self):
        for car in self.car_storage:
            new_x_cord = car.xcor() - self.distance
            car.goto(new_x_cord, car.ycor())

    def increase_speed(self):
        self.distance += 10
