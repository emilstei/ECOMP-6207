import turtle
import random

star = turtle.Turtle()

star.speed(0)
turtle.bgcolor('purple')

for i in range(25):#create many, many starbursts
    #get color
    turtle.colormode(255)
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    star.color(red, green, blue)
    #random position
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    star.penup()
    star.setposition(x,y)
    star.pendown()
    #change the size
    size = random.randint(10,200)
    star.begin_fill()
    while True:
        star.forward(size)
        star.left(145)
        if star.heading()==0:
            break
    star.end_fill()
turtle.done()


