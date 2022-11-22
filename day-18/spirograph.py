import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
screen = Screen()

i = 0
tim.speed(0)
screen.colormode(255)
tim.pensize(8)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def draw_spirograph(size_of_grap):
    for _ in range(int(360 / size_of_grap)):
        tim.color(random_color())
        tim.circle(80)
        tim.setheading(tim.heading() + size_of_grap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()