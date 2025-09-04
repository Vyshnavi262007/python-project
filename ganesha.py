import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Beautiful Lord Ganesha - Turtle Art")
t = turtle.Turtle()
t.speed(10)
t.pensize(2)

def draw_circle(color, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()

def draw_trunk():
    t.color("orange")
    t.fillcolor("orange")
    t.penup()
    t.goto(0, -40)
    t.pendown()
    t.begin_fill()
    t.right(90)
    t.circle(30, 180)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.circle(30, 180)
    t.end_fill()
    t.penup()
    t.setheading(0)

def draw_ears():
    draw_circle("orange", -130, 20, 60)
    draw_circle("orange", 130, 20, 60)

def draw_eyes():
    draw_circle("white", -35, 50, 12)
    draw_circle("white", 35, 50, 12)
    draw_circle("black", -35, 55, 5)
    draw_circle("black", 35, 55, 5)

def draw_crown():
    draw_circle("gold", 0, 140, 50)

def draw_modak(x, y):
    draw_circle("yellow", x, y, 15)

def draw_body():
    draw_circle("orange", 0, -100, 100)

# Drawing Ganesha
draw_body()
draw_ears()
draw_crown()
draw_eyes()
draw_trunk()
draw_modak(-150, -50)
draw_modak(150, -50)

# Decorative tilak
t.goto(-10, 120)
t.pendown()
t.color("red")
t.pensize(5)
t.forward(20)
t.penup()

# Signature
t.goto(300, -300)
t.color("white")
t.write("Beautiful Ganesha by Turtle", font=("Arial", 12, "normal"))

t.hideturtle()
turtle.done()
