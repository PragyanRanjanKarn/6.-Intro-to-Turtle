import turtle
s = turtle.Screen()
s.setup(300,300)
s.bgcolor("white")
turtle.title("Welcome to Turtle Window")
t = turtle.Turtle()

# 1) Square
for i in range(4):
    t.forward(100)
    t.left(360/4)


# 2) Triangle
for i in range(3):
    t.forward(100)
    t.left(360/3)


# 3) Pentagon
for i in range(5):
    t.forward(100)
    t.left(360/5)

# 4) Hexagon
for i in range(6):
    t.forward(100)
    t.left(360/6)


# 5) Rectangle
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)


# 6) Circle
for i in range(360):
    t.forward(2)
    t.left(360/360)


t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

t.penup()
t.right(150)

t.forward(50)
t.pendown()

t.right(90)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)

# Creating a square
colors = ["red","orange","yellow","green","blue"]
x = 1
y = 0
t.speed("fastest")
for i in range(5): # 5 times
    for j in range(20): # 20 times
        t.goto(0,0)
        t.pencolor(colors[y])
        for k in range(360):
            t.forward(x)
            t.right(1)
        t.left(18)
    x += 1
    if y<colors.length-1:
        y += 1
    else:
        y = 0


        
turtle.done()

