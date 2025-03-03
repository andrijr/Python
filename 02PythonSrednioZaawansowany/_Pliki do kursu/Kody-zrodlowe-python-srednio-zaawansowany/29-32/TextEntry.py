import tkinter as t

def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

window = t.Tk()
window.title("Różnica silnii")

def closeWindow():
    window.destroy()

t.Label(window,text="Podaj dwie liczby naturalne oddzielone spacją (np. 7 4)").pack(side=t.TOP, padx=10, pady=10)

entry = t.Entry(window, width=10)
entry.pack(side=t.TOP, padx=10, pady=10)

answer = t.Label(window, text="Odpowiedź: ")
answer.pack(side=t.TOP, padx=10, pady=10)

def getValues():
    x, y = [int(x) for x in entry.get().split(' ')]
    result = factorial(x) - factorial(y)
    print(result)
    answer['text'] = "Odpowiedź: " + str(result)


t.Button(window, text="OK", command=getValues).pack(side=t.LEFT)
t.Button(window, text="CLOSE", command=closeWindow).pack(side=t.RIGHT)

window.mainloop()