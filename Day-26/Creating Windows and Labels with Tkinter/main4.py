from tkinter import *

window = Tk()
window.title('Training Tkinter')
window.minsize(height= 500, width= 500)


label =Label(text="My try Text")
label.config(text='My NEW Text')
label.pack()

def action():
    print('Do something')

button = Button(text="Click Me", command=action)
button.pack()

entry = Entry(width=33)
entry.insert(index=END, string="Some text to begin with.")
print(entry.get())
entry.pack()

text = Text(height=5, width=25)
text.focus()
text.insert(END, 'Example of Multi-line text entry.')
print(text.get('1.0', END))
text.pack()

def spin_box():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, command=spin_box, width=5)
spinbox.pack()

def scale_box(valve):
    print(valve)

scale = Scale(from_=0, to=50, command=scale_box)
scale.pack()

def check_use():
    print(check.get())

check = IntVar()
checkbutton = Checkbutton(text='is on', variable=check, command=check_use)
check.get()
checkbutton.pack()

def radio_use():
    print(radio.get())

radio= IntVar()
radiobutton1 = Radiobutton(text='option1', value=1, variable=radio, command=radio_use)
radiobutton2 = Radiobutton(text='option1', value=2, variable=radio, command=radio_use)
radio.get()
radiobutton1.pack()
radiobutton2.pack()


def list_use(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=5)
fruits =['Apple', 'Banana', 'Orange', 'Mango', 'Pear']
for i in fruits:
    listbox.insert(fruits.index(i), i)
listbox.bind("<<ListboxSelect>>", list_use)
listbox.pack()


window.mainloop()