import math
import turtle

# Set the background color to light blue
turtle.bgcolor("lightblue")

tina = turtle.Turtle()
tina.shape("turtle")
tina.color("black")
tina.speed(0)

# Function to write "lov u" at the beginning
def write_lov_u():
    tina.penup()
    tina.goto(0, 200)  # Adjust the coordinates for the position of the text
    tina.pendown()
    tina.color("red")  # You can adjust the color
    tina.write("lov u Chio ❤️", align="center", font=("Comic Sans MS", 36, "normal"))
    tina.penup()
    tina.goto(0, 0)  # Return the turtle to the center

def drawSunflower(t, numseeds, numpetals, angle, cspread):
    t.fillcolor("orange")
    phi = angle * (math.pi / 180.0)
   
    for i in range (numseeds + numpetals):
        # figure out the next x, y position
        r = cspread * math.sqrt(i)
        theta = i * phi
        x = r * math.cos(theta)
        y = r * math.sin(theta)

        # move the turtle and orient it correctly
        t.penup()
        t.goto(x, y)
        t.setheading(i * angle)
        t.pendown()

        if i <  numseeds:
            t.stamp()
        else:
            drawPetal(t)

def drawPetal(t):
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(20)
    t.forward(70)
    t.left(40)
    t.forward(70)
    t.left(140)
    t.forward(70)
    t.left(40)
    t.forward(70)
    t.end_fill()

def drawStem(t):
    t.penup()
    t.goto(0, -350)  # Adjust the coordinates as needed for the stem length
    t.pendown()
    t.color("green")
    t.pensize(15)
    t.setheading(90)  # Point the turtle upward
    t.forward(200)    # Adjust the stem length as needed
    # reset color and pensize for the flower
    t.color("black")
    t.pensize(1)

def drawHappyFace(t):
    t.penup()
    t.goto(0, -30)  # Adjust the coordinates for the position of the face
    t.pendown()
    

    # Draw the left eye (a white circle with a black outline)
    t.penup()
    t.goto(-20, 20)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    # Draw the right eye (a white circle with a black outline)
    t.penup()
    t.goto(20, 20)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    # Draw the mouth (a half-circle)
    t.penup()
    t.pensize(5)
    t.pendown()
    t.color("black")
    t.setheading(0)  # Point the turtle right

    t.penup()
    t.goto(-40, 15)  # Move to the starting point for the new smile
    t.pendown()
    t.right(90)
    t.circle(40, 180)
    t.penup()



write_lov_u()
drawStem(tina)
drawSunflower(tina, 160, 40, 137.508, 4)
drawHappyFace(tina)

tina.hideturtle()
turtle.done()
