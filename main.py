import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("tan")

t = turtle.Turtle()
t.speed(5)

t.pencolor("blue")
t.penup()
t.goto(-80,15)
t.pendown()
t.circle(35)
t.pencolor("black")
t.penup()
t.goto(0,15)
t.pendown()
t.circle(35)
t.pencolor("red")
t.penup()
t.goto(80,15)
t.pendown()
t.circle(35)
t.pencolor("yellow")
t.penup()
t.goto(-40,-15)
t.pendown()
t.circle(35)
t.pencolor("green")
t.penup()
t.goto(40,-15)
t.pendown()
t.circle(35)





turtle.done()