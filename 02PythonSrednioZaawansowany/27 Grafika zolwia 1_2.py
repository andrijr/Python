import turtle # grafika żółwia

zolw1 = turtle.Turtle()
# zolw1.shape('')
zolw1.pencolor("red")
zolw1.speed(2)
zolw1.color('red', 'yellow')
zolw1.begin_fill() # wypełnienie kolorem
for i in range(6):
    zolw1.forward(100)
    zolw1.right(60)
zolw1.end_fill() # wypełnienie kolorem
turtle.done()