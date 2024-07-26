from turtle import Turtle


class Object(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.setposition(0, -280)
        self.setheading(90)

    def up(self):
        new_y_cord = self.ycor() + 20
        self.goto(self.xcor(), new_y_cord)
