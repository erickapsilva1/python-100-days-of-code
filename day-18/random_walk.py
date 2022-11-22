import turtle as t
import random

tim = t.Turtle()
tim.pensize(5)

steps = 1
directions = [0, 90, 180, 270]

while True:
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)

    tim.forward(30)
    tim.setheading(random.choice(directions))



