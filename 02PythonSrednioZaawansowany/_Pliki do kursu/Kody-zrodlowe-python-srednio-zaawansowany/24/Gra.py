from sfml import sf
from Board import Board

###########
###INTRO###
###########

NORMAL_RESOLUTION = 600
RESOLUTION_X = 600
RESOLUTION_Y = 600
START_MOUSE_POSITION = -1
SIZE_BOARD = 9

window = sf.RenderWindow(sf.VideoMode(RESOLUTION_X,RESOLUTION_Y),"Kółko i krzyżyk")

textureX = sf.Texture.from_file('Grafika/X.png')
textureO = sf.Texture.from_file('Grafika/O.png')
textureP = sf.Texture.from_file('Grafika/PLUS.png')

arrayX = []
for i in range(SIZE_BOARD):
    sprite = sf.Sprite(textureX)
    arrayX.append(sprite)

arrayO = []
for j in range(SIZE_BOARD):
    sprite = sf.Sprite(textureO)
    arrayO.append(sprite)

arrayP = []
for k in range(SIZE_BOARD):
    sprite = sf.Sprite(textureP)
    arrayP.append(sprite)

objectBoard = Board("X")

mousePosition = sf.Vector2(START_MOUSE_POSITION,START_MOUSE_POSITION)

while window.is_open:
    window.clear(sf.Color.BLUE)

    for event in window.events:
        pass

    if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
        window.close()

    board = objectBoard.returnBoard()

    if sf.Mouse.is_button_pressed(0):
        mousePosition = sf.Mouse.get_position()
    betterMousePosition = mousePosition - window.position

    if betterMousePosition.x > 0 and betterMousePosition.y > 0:
        if betterMousePosition.x < RESOLUTION_X*(1/3):
            if betterMousePosition.y < RESOLUTION_Y*(1/3):
                objectBoard.putToBoard(1,1)
            elif betterMousePosition.y < RESOLUTION_Y*(2/3):
                objectBoard.putToBoard(2,1)
            else:
                objectBoard.putToBoard(3,1)
        elif betterMousePosition.x < RESOLUTION_X*(2/3):
            if betterMousePosition.y < RESOLUTION_Y*(1/3):
                objectBoard.putToBoard(1,2)
            elif betterMousePosition.y < RESOLUTION_Y*(2/3):
                objectBoard.putToBoard(2,2)
            else:
                objectBoard.putToBoard(3,2)
        else:
            if betterMousePosition.y < RESOLUTION_Y*(1/3):
                objectBoard.putToBoard(1,3)
            elif betterMousePosition.y < RESOLUTION_Y*(2/3):
                objectBoard.putToBoard(2,3)
            else:
                objectBoard.putToBoard(3,3)


    ###############
    ###RYSOWANIE###
    ###############

    rectangle1 = sf.RectangleShape()
    rectangle1.size = (RESOLUTION_X,0)
    rectangle1.outline_color = sf.Color.RED
    rectangle1.outline_thickness = 5
    rectangle1.position = (0,RESOLUTION_Y*(1/3))

    rectangle2 = sf.RectangleShape()
    rectangle2.size = (RESOLUTION_X,0)
    rectangle2.outline_color = sf.Color.RED
    rectangle2.outline_thickness = 5
    rectangle2.position = (0,RESOLUTION_Y*(2/3))

    rectangle3 = sf.RectangleShape()
    rectangle3.size = (0,RESOLUTION_Y)
    rectangle3.outline_color = sf.Color.RED
    rectangle3.outline_thickness = 5
    rectangle3.position = (RESOLUTION_X*(1/3),0)

    rectangle4 = sf.RectangleShape()
    rectangle4.size = (0,RESOLUTION_Y)
    rectangle4.outline_color = sf.Color.RED
    rectangle4.outline_thickness = 5
    rectangle4.position = (RESOLUTION_Y*(2/3),0)

    window.draw(rectangle1)
    window.draw(rectangle2)
    window.draw(rectangle3)
    window.draw(rectangle4)

    toDraw = []
    for aX in range(3):
        for aY in range(3):
            if board[aX][aY] == '*':
                arrayP[3 * aX + aY].position = sf.Vector2(RESOLUTION_X*(1/3) * aY, RESOLUTION_Y*(1/3) * aX)
                toDraw.append(arrayP[3 * aX + aY])
            elif board[aX][aY] == 'X':
                arrayX[3 * aX + aY].position = sf.Vector2(RESOLUTION_X*(1/3) * aY, RESOLUTION_Y*(1/3) * aX)
                toDraw.append(arrayX[3 * aX + aY])
            else:
                arrayO[3 * aX + aY].position = sf.Vector2(RESOLUTION_X*(1/3) * aY, RESOLUTION_Y*(1/3) * aX)
                toDraw.append(arrayO[3 * aX + aY])

    for elementToDraw in range(9):
        window.draw(toDraw[elementToDraw])

    window.display()

    ################
    ###SPRZĄTANIE###
    ################

    mousePosition.x = START_MOUSE_POSITION
    mousePosition.y = START_MOUSE_POSITION

    if objectBoard.checkIfWin() or objectBoard.checkIfDraw():
        break

if objectBoard.checkIfDraw():
    print("REMIS")
else:
    if objectBoard.getPlayer() == 'O':
        print("Wygrał gracz grający krzyżykami")
    else:
        print("Wygrał gracz grający kółkami")