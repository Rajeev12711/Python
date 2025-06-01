from tkinter import *


window = Tk()
window.title("Mile to Km converter")
window.minsize(height=100, width=290)
window.config(padx=20, pady=20)


def calculate_button():
    answer = round(float(textbox.get()) * 1.609)
    km_result.config(text=f"{answer}")


mile = Label(text='Mile')
mile.config(padx=10, pady=10)
mile.grid(column=2, row=0)


equal = Label(text='Is equal to')
equal.config(padx=10, pady=10)
equal.grid(column=0, row=1)


textbox = Entry(width=15)
textbox.grid(column=1, row=0)


km_result = Label(text='0')
km_result.grid(column=1, row=1)


km = Label(text='KM')
km.config(padx=10, pady=10)
km.grid(column=2, row=1)


calculate = Button(text='Calculate', command=calculate_button)
calculate.grid(column=1, row=2)


window.mainloop()