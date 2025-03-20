import turtle

def draw_heart():
    turtle.color("red")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

def move_heart_up():
    turtle.penup()
    turtle.goto(0, 90)  # Move up by 90 pixels
    turtle.pendown()
    draw_heart()
    turtle.done()

move_heart_up()