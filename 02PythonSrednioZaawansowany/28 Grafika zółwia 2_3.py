
import turtle

zolw = turtle.Turtle()
zolw.speed(100)
zolw.penup() # zółw w powietrzu
for i in range(10):
    for i in range(5):
        zolw.dot(5, 'red')
        zolw.forward(10)
        zolw.dot(2, 'red')
    zolw.backward(5*10) # powrót
    zolw.goto(zolw.position()[0], zolw.position()[1]-10)


turtle.done()