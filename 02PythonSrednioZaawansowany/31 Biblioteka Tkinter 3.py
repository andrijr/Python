import tkinter as t

def factorial(n):
    product =1
    for i in range(1,n+1):
        product *= i
    return product

window1 = t.Tk()
window1.title("Różnica silnii")

def closeWindow():
    window1.destroy()

t.Label(window1, text="podaj dwie liczby naturalne oddzielone spacja np. 7, 4").pack(side=t.TOP, padx=10, pady=10)
entry1 = t.Entry(window1, width=10)
entry1.pack(side=t.TOP, padx=10, pady=10)

answer1 = t.Label(window1, text="Odpowiedź")
answer1.pack(side=t.TOP, padx=10, pady=10)

def getValues():
    x,y = [int(x) for x in entry1.get().split(" ")]
    result = factorial(x) - factorial(y)
    print(result)
    answer1["text"] = "Odpowiedź " + str(result)


t.Button(window1, text="OK", command=getValues).pack(side=t.LEFT)
t.Button(window1, text="Close", command=closeWindow).pack(side=t.RIGHT)

window1.mainloop()

