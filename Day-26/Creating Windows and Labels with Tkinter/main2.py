import tkinter
from tkinter.ttk import Button

window = tkinter.Tk()

window.title("First Tk")
window.minsize(width=500, height=300)

window = tkinter.Label(text= "My first tkinter Page", font=("arial", 24, 'bold') )
window.pack(side='top')


window['text'] ="NEW TEXT"
window.config(text='NEW TEXT')


def clicked():
    print("Successfully")

button = Button(text="Submit", command=clicked)
button.pack()

window.mainloop()