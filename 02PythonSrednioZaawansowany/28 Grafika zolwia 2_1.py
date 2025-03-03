import turtle

zolw1 = turtle.Turtle()
zolw1.pencolor('orange')
zolw1.speed(10000)
for i in range(120):
    zolw1.forward(150)
    zolw1.right(4)
    zolw1.forward(150)
    zolw1.left(4)
    zolw1.forward(100)
    zolw1.penup()
    zolw1.setposition(0,0) # zolw1.goto(0,0) robi to samo powraca do pierwotnej pozycji
    zolw1.pendown()
    zolw1.right(3)
turtle.done()