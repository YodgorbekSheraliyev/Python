BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import random
import pandas
import json


try:
    data = pandas.read_csv("./to_learn.csv")
    word_list = data.to_dict(orient="records")

except FileNotFoundError as f:
    data = pandas.read_csv("./data/french_words.csv")
    word_list = data.to_dict(orient="records")
    data.to_csv("to_learn.csv", index=False)

current_card = {}


def remove_word():
    print(len(word_list))
    global current_card
    if current_card in word_list:
        word_list.remove(current_card)
    data = pandas.DataFrame(word_list)
    data.to_csv('to_learn.csv', index=False)


def next():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_list)
    card.itemconfigure(card_word, text=current_card["French"])
    card.itemconfigure(card_text, text="French")
    card.itemconfigure(card_img, image=card_img_front)
    flip_timer = window.after(3000, flip_card)


def is_next():
    remove_word()
    next()


def flip_card():
    card.itemconfigure(card_text, text="English")
    card.itemconfigure(card_word, text=current_card["English"])
    card.itemconfigure(card_img, image=card_img_back)


def reset():
    card.itemconfigure(card_text, text="French")
    card.itemconfigure(card_img, image=card_img_front)


window = Tk()
window.configure(bg=BACKGROUND_COLOR, width=1000, height=800, padx=50, pady=50)
window.title("Flashy")
flip_timer = window.after(3000, flip_card)

card_img_front = PhotoImage(file="./images/card_front.png")
card_img_back = PhotoImage(file="./images/card_back.png")
card_img_width = card_img_front.width()
card_img_height = card_img_front.height()

card = Canvas(
    width=card_img_width,
    height=card_img_height,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
)
card_img = card.create_image(
    card_img_width / 2, card_img_height / 2, image=card_img_front
)
card_text = card.create_text(
    card_img_width / 2, 150, text="French", font=("Arial", 40, "italic")
)
card_word = card.create_text(
    card_img_width / 2, card_img_height / 2, text="Word", font=("Arial", 60, "bold")
)
card.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(
    image=wrong_img, highlightthickness=0, border=0, borderwidth=0, command=next
)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="./images/right.png")
known_button = Button(
    image=check_img, highlightthickness=0, border=0, borderwidth=0, command=is_next
)
known_button.grid(row=1, column=1)

next()
window.mainloop()
