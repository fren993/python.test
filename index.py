#hello
import turtle

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set drawing speed to fastest

# Set color
t.color("red")

# Start filling
t.begin_fill()

# Draw the heart
t.left(45)
t.forward(100)
t.circle(50, 180)
t.right(90)
t.circle(50, 180)
t.forward(100)

# End filling
t.end_fill()

# Keep the window open
turtle.done()