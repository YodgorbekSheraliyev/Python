# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
FONT =("Arial", 12, "normal")
from tkinter import *
from tkinter import messagebox
import pyperclip
import string
from random import randint, shuffle, choice


window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)

img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(img.width()/2, img.height()/2, image=img)
canvas.grid(column=1, row=0)

# labels
label_name = Label(text="Website: ",  font=FONT)
label_name.grid(column=0, row=1)

label_email = Label(text="Email/Username: ",  font=FONT)
label_email.grid(column=0, row=2)

label_password = Label(text="Password: ",  font=FONT)
label_password.grid(column=0, row=3)

# entries
website_entry = Entry(font=FONT, width=35)
website_entry.grid( column=1, row=1 , columnspan=2,)

label_email_entry = Entry(font=FONT, width=35)
label_email_entry.grid( column=1, row=2 , columnspan=2,)
label_email_entry.insert(0, "johdoe@mail.com")

password_entry = Entry(font=FONT, width=22)
password_entry.grid( column=1, row=3)



def generate_password():
    letters_list =list(string.ascii_letters)
    symbols_list = ["!","@","#","$","%","^","&","*","(",")", "_", "=", "+", "-"]
    num_list = [0,1,2,3,4,5,6,7,8,9]

    letters = [choice(letters_list) for _ in range(randint(6, 8))]
    symbols = [choice(symbols_list) for _ in range(randint(6, 8))]
    nums = [f"{choice(num_list)}" for _ in range(randint(6, 8))]

    password_list = letters + symbols + nums
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    website_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)

def write_to_file():
    website_name = website_entry.get()
    email = label_email_entry.get()
    password = password_entry.get()

    if len(website_name) ==0 or len(password) ==0 :
        messagebox.showwarning(title="Warning", message="Please fill all fields")

    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the website details: \n Website: {website_name} \n Email: {email}\n Password: {password}")
        if is_ok: 
            with open('data.txt', 'a') as file:
                text = f"{website_name.capitalize()} | {email} | {password}"
                file.write(f'{text} \n')

            website_entry.delete(0, END)
            password_entry.delete(0, END)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=write_to_file)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()