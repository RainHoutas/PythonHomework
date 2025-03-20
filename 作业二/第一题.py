import turtle

def draw_filled_triangle():
    turtle.color("blue")  # Set the fill color
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(100)  # Length of each side
        turtle.left(120)  # Angle for equilateral triangle
    turtle.end_fill()
    turtle.done()

draw_filled_triangle()