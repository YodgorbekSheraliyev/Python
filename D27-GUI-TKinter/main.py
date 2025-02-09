import  tkinter

window = tkinter.Tk()
window.title("TKINTER")
window.minsize(500, 300)

my_label = tkinter.Label(text=" I am a Label", font=("Arial", 24, "bold"))
my_label.pack()


button = tkinter.Button(text="Click Me")
input = tkinter.Entry(width=10)
button.pack()
input.pack()

def change_label():
    text = input.get()
    my_label.configure(text=text)
button.configure(command=change_label)


window.mainloop()