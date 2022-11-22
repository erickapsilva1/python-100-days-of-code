import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
screen = Screen()

tim.pensize(8)
directions = [0, 90, 180, 270]
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


while True:
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))



