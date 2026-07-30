import turtle

# Create a turtle object
t = turtle.Turtle()
t.speed(2)  # Set turtle speed
t.shape("turtle")
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
# #List of colors
colors = ["red", "blue", "green", "orange"]
#   # Fill inside the square with yellow
t.begin_fill()
# #
for i in range(4):
    t.color(colors[i])
    t.forward(200)
    t.left(90)
# #
t.fillcolor("pink")
t.end_fill()
t.color("pink")
t.forward(150)
t.left(90)
t.color("orange")
t.forward(100)
#
t.color("green")
t.fillcolor("blue")
t.begin_fill()
t.circle(50)
t.end_fill()

turtle.done()