import turtle
from itertools import cycle
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
shelly = turtle.Turtle()
def draw_circle(size):
    shelly.pencolor(next(colors))
    shelly.circle(size)
    draw_circle(size + 5)
turtle.bgcolor('black')
shelly.speed('fast')
shelly.pensize(4)
shelly.pencolor('purple')
draw_circle(30)

