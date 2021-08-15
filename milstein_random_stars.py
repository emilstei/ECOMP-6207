import turtle as t
from random import randint, random

points = 7

def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range (points):
        t.forward(size)
        t.right(angle)
    t.end_fill() #stops the fill color

#setting the background color
t.Screen().bgcolor('dark blue')


while True:
    ranSize = randint(10, 35)
    ranCol = (random(), random(), random())
    ranX = randint(-200, 200)
    ranY = randint(-200, 200)

draw_star(points, ranSize, ranCol, ranX, ranY)
