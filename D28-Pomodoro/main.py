# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 1

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Pomdoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

timer_label = Label(
    text="Timer", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 45, "normal")
)
timer_label.grid(column=1, row=0)


count_down_id = 0
def count_down(count):
    global count_down_id
    minutes = 0
    seconds = 0
    if 0<=(count //60) <=9:
        minutes = f"0{count//60}"
    else:
        minutes = count//60
    if 0<=(count %60) <=9:
        seconds = f"0{count%60}"
    else:
        seconds = count%60
    canvas.itemconfigure(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        count_down_id = window.after(1000, count_down, count - 1)


def start_timer():
    global rep
    if rep in [1,3,5,7] :
        count_down(WORK_MIN * 60)
        timer_label.configure(text="Timer")
        rep+=1
    elif rep in [2,4,6]:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.configure(text="Break")
        rep +=1
    elif rep is 8:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.configure(text="Long Break")
        rep = 1
    else:
        rep +=1
        count_down(WORK_MIN * 60)
        


def reset_timer():
    global rep
    canvas.itemconfigure(timer_text, text="00:00")
    window.after_cancel(count_down_id)
    rep = 1

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

tick1 = Label(text="1")
tick1.grid(column=1, row=3)

window.mainloop()
