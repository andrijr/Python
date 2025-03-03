import tkinter as t
import itertools

def attack(List2D,n):
    for row in List2D:
        for i in range(1,n):
            if [row[0]+i,row[1]+i] in List2D:
                return True
            if [row[0]+i,row[1]-i] in List2D:
                return True
            if [row[0]-i,row[1]+i] in List2D:
                return True
            if [row[0]-i,row[1]-i] in List2D:
                return True
    return False

def numberOfQueens(n):
    coordinates =  [x for x in range(n)] #Lista współrzędnych typu: [0,1,2,3,4,5,6,7]
    permutations = [list(x) for x in itertools.permutations(coordinates)]
    #print(permutations)
    answer = 0
    for combination in permutations:
        Queens2DList = [[i,combination[i]] for i in range(n)]
        if not attack(Queens2DList,n):
            answer += 1
    return answer

window = t.Tk()
window.title("Problem n hetmanów")

def closeWindow():
    window.destroy()

t.Label(window,text="Podaj liczbę naturalną oznaczającą wymiar szachownicy (np. 8)").pack(side=t.TOP, padx=10, pady=10)

entry = t.Entry(window, width=10)
entry.pack(side=t.TOP, padx=10, pady=10)

answer = t.Label(window, text="Odpowiedź: ")
answer.pack(side=t.TOP, padx=10, pady=10)

def getValues():
    n = int(entry.get())
    result = numberOfQueens(n)
    print(result)
    answer['text'] = "Odpowiedź: " + str(result)


t.Button(window, text="OK", command=getValues).pack(side=t.LEFT)
t.Button(window, text="CLOSE", command=closeWindow).pack(side=t.RIGHT)

window.mainloop()