import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
screen = Screen()

i = 0
tim.speed(10)
screen.colormode(255)
tim.pensize(8)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


while True:
    tim.color(random_color())
    tim.circle(80)
    tim.setheading(i)
    i += 10
