from tkinter import *
import math

window = Tk()
window.title("Mile to Kilometer Converter")
# window.minsize(width=500, height=100)
window.configure(padx=50, pady=50)

entry = Entry(width=10)
entry.insert(END, 0)
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

label = Label(text="is equal to")
label.grid(column=0, row=1)

value_label = Label(text="0")
value_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

def calculate():
    entry_input = int(entry.get())
    value_label.configure(text= round(entry_input * 1.6, 2))

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)




window.mainloop()