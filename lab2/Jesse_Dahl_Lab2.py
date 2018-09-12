import turtle
import random

window = turtle.Screen()

square = turtle.Turtle()
square.speed(0)
square.hideturtle()

square.up()
square.goto(-200, 200)
square.down()

for i in range(4):
    square.forward(50)
    square.right(90)

square.up()
square.goto(-205, 205)
square.write("Change Color")

square.up()
square.goto(200,200)
square.down()

for i in range(4):
    square.forward(50)
    square.right(90)

square.up()
square.goto(195,205)
square.write("Move Mouse")
        
pencil = turtle.Turtle()
pencil.shape("circle")

def drawing_controls(x,y):
    if (-200 <= x <= -150) and (150 <= y <= 200):
        red = random.random()
        green = random.random()
        blue = random.random()
        pencil.color(red, green, blue)
    elif (200 <= x <= 250) and (150 <= y <= 200):
        pencil.up()
        x_chor = random.randint(-300,300)
        y_chor = random.randint(-300,300)
        pencil.goto(x_chor, y_chor)
        pencil.down()


window.onclick(drawing_controls)

pencil.onrelease(pencil.goto)
        
