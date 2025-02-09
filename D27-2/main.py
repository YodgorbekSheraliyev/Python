from tkinter import *

window = Tk()
window.title("Widgets")
window.minsize(500, 500)

# Label
label = Label(text="This is old text")
label.configure(text="This is new text")
label.pack()

# Buttons
def action():
    print("Do something")

# calls action() when button clicked
button = Button(text="Button", command=action)
button.pack()

# Entry
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with")
# Gets text in entry
entry_text = entry.get()
entry.pack()

# Text
text = Text(height=5, width=50)
# Puts cursor in textbox
text.focus()
text.insert(END, "Example of multi-line text entry.")
# Gets the current value in textbos at line 1, character 0
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutoon
def checkbutton_used():
    # Prints 1 if on buton checked otherwise 0
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())

#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
