import tkinter

window1 = tkinter.Tk()

window1.title("Moje 1 Okienko")
# # window.geometry("800x600+miejsce_na_x+miejsce_na_y")
window1.geometry("800x600+400+100")
# print("nie działa zwykłe printowanie")
myLabel = tkinter.Label(window1, text="Moja pierwsza labelka", fg='red', bg='yellow', width='50', font=("Arial", 16), anchor='e',
                       height=2 )

myLabel.pack()
#myLabel.place(x=100,y=100)
myLabel.place(relx=0, rely=0.50)
window1.mainloop()


window2 = tkinter.Tk()
window2.geometry("800x600+200+100")
myLabel = tkinter.Label(window2, text="Moja pierwsza labelka")
window2.mainloop()