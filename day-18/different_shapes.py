from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

angles = 4

for _ in range(7):
    R = random.random()
    B = random.random()
    G = random.random()

    for _ in range(angles):
        timmy_the_turtle.color(R, G, B)
        degrees = 360 / angles
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(degrees)
    angles += 1

screen = Screen()
screen.exitonclick()

