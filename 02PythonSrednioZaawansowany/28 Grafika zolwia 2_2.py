
import turtle

zolw = turtle.Turtle()
zolw.color('red', 'yellow')
zolw.speed(50)
zolw.begin_fill()
while True:
     zolw.forward(200)
     zolw.left(170)
     if abs(zolw.pos()) < 1:
         break
zolw.end_fill()
turtle.done()