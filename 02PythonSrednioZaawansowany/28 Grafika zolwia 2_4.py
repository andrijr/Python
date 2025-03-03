import turtle

zolw = turtle.Turtle()

window = turtle.Screen()
window.bgcolor("green") # kolor tła  okna
zolw.shape("circle") # typ znacznika
zolw.color('blue') # color wypełnienia
size = 10
zolw.penup() # podniesienie zółwia
zolw.speed(100)
for i in range(100):
    zolw.stamp() # postawienie żółwia
    size += 3
    zolw.forward(size) # ruch do przodu
    zolw.right(20) # kąt skręcenia


turtle.done()