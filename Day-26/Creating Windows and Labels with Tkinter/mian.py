import tkinter

window = tkinter.Tk()

window.title("First Tk")
window.minsize(width=500, height=300)

window = tkinter.Label(text= "My first tkinter Page", font=("arial", 24, 'bold') )
window.pack(side='top')

window.mainloop()