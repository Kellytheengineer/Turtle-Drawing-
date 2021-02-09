# Let's draw some cool drawings with the package turtle
# Import turtle
import turtle
# Let's get a nice set up in turtle
turtle.bgcolor("black") # Background colour
turtle.pensize(2) # Pen size
turtle.speed(0)
turtle.color("red")

# Advanced spiral
for i in range(6):
   for colours in ["red", "orange", "yellow", "green", "blue", "purple"]: # Put colours into for loop spiral
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(10)

turtle.done()

