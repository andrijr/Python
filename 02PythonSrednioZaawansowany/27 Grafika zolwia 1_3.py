import turtle # grafika żółwia

zolw1 = turtle.Turtle()
# zolw1.shape('')
zolw1.pencolor("red")
zolw1.speed(3)
colors = ['blue','green','brown','silver','black','purple','pink','gray','red','white']
for j in range(10):
    zolw1.begin_fill()
    for i in range(6):
        zolw1.forward(100-10*j)
        zolw1.right(60)
    zolw1.end_fill()
    zolw1.color('red', colors[j])
    zolw1.pencolor(colors[j-1 ])
    zolw1.goto(zolw1.position()[0]+5,zolw1.position()[1]-8)

turtle.done()