import turtle
s = turtle.Screen()
s.setup(300,300)
s.bgcolor("pink")
turtle.title("Welcome to Turtle Window")
t = turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.left(360/4)
t.right(5)
