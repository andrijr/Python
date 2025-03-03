# import turtle
# zolw = turtle.Turtle()
# zolw.pencolor('red')
# zolw.speed(2)
# zolw.color('red','yellow')
# zolw.begin_fill()
# for i in range(6):
#     zolw.forward(100)
#     zolw.right(60)
# zolw.end_fill()
# turtle.done()

import turtle
zolw = turtle.Turtle()
zolw.shape('turtle')
colors = ['blue','green','brown','silver','black','purple','pink','gray','red','white']
zolw.color('red','yellow')
for j in range(10):
    zolw.begin_fill()
    for i in range(6):
        zolw.forward(100-10*j)
        zolw.right(120)
    zolw.end_fill()
    zolw.color('red',colors[j])
    zolw.pencolor(colors[j-1])
    zolw.goto(zolw.position()[0]+5,zolw.position()[1]-8)
    zolw.pencolor('red')
turtle.done()