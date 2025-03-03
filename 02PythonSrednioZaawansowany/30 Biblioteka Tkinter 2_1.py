import tkinter as t

window1 = t.Tk()
window1.title("Moje 1 Okienko")

def buttonClicked():
    label = t.Label(window1, text="labelka")
    label.pack()

frame1 = t.Frame(window1,  width=40, height=40, bg='yellow')
frame1.pack_propagate(0)
frame1.pack()
button1 = t.Button(window1, text='OK', state="active", command=buttonClicked)
button1.pack(fill='both', expand=1, padx=10, pady=5)
window1.mainloop()

