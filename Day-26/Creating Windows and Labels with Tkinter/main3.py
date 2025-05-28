import tkinter
from tkinter.ttk import Button, Entry

window = tkinter.Tk()

window.title("First Tk")
window.minsize(width=500, height=300)

window = tkinter.Label(text= "My first tkinter Page", font=("arial", 24, 'bold') )
window.pack(side='top')


window['text'] ="NEW TEXT"
window.config(text='NEW TEXT')


def clicked():
    new_input = Text.get()
    window.config(text=new_input)


button = Button(text="Submit", command=clicked)
button.pack()


Text = Entry(width=10)
Text.pack()
print(Text.get())



window.mainloop()