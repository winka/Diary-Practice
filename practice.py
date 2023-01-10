import turtle

# setup
turtle.setup(600,600)
turtle.pensize(20)
turtle.bgcolor('black')

# column
for i in range(5):
    turtle.penup()
    turtle.color('white')
    turtle.goto(-200+i*100, 300)
    turtle.setheading(270)
    turtle.pendown()
    turtle.forward(600)
# index
for i in range(5):
    turtle.penup()

    turtle.color('white')
    turtle.goto(-300, -200+i*100)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(600)

turtle.done()