import tkinter as t

window = t.Tk()
window.title("Moje okno")

def buttonClicked():
    label = t.Label(window, text="Labelka")
    label.pack()

frame = t.Frame(window, width=80, height=40, bg="red")
frame.pack_propagate(0)
frame.pack()

button = t.Button(frame, text="Ok", command=buttonClicked)
button.pack(fill="both", expand=1, padx=10, pady=2)

window.mainloop()