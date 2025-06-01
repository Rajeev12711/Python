from tkinter import *

window = Tk()
window.title('Grid')
window.minsize(height=500, width=500)
window.config(padx=50,pady=50)


label = Label(text='label')
label.config(text="NEW TASK")
label.grid(column=0, row=0)
label.config(padx=20, pady=20)


button = Button(text="Click me")
button.grid(column=1, row=1)


button2 = Button(text="Click me")
button2.grid(column=2, row=0)

textbox= Entry(width=10)
textbox.grid(column=3,row=2)

window.mainloop()