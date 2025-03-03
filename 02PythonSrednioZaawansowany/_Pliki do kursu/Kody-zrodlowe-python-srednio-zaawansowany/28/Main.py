# import turtle
#
# zolw = turtle.Turtle()
# zolw.pencolor("orange")
# zolw.speed(100)
# for i in range(120):
#     zolw.forward(150)
#     zolw.right(4)
#     zolw.forward(150)
#     zolw.left(4)
#     zolw.forward(100)
#     zolw.penup()
#     zolw.goto(0,0)
#     zolw.pendown()
#     zolw.right(3)
#
# turtle.done()

# import turtle
# zolw = turtle.Turtle()
# zolw.color('red', 'yellow')
# zolw.speed(5)
# zolw.begin_fill()
# while True:
#     zolw.forward(200)
#     zolw.left(170)
#     if abs(zolw.pos()) < 1:
#         break
# zolw.end_fill()
# turtle.done()


# import turtle
# zolw = turtle.Turtle()
#
# zolw.penup()
# for i in range(10):
#     for j in range(5):
#         zolw.dot()
#         zolw.forward(10)
#     zolw.backward(5*10)
#     zolw.goto(zolw.pos()[0],zolw.pos()[1]-10)
# turtle.done()


import turtle
zolw = turtle.Turtle()
window = turtle.Screen()
window.bgcolor('green')
zolw.shape('turtle')
zolw.color('blue')
size = 10
zolw.penup()
zolw.speed(5)
for i in range(150):
    zolw.stamp()
    size += 1
    zolw.forward(size)
    zolw.right(30)
turtle.done()