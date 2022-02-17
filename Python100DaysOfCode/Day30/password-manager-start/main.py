from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_NAME = "Arial"
FONT_SIZE = 8


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    input_password.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)
    password_list = "".join(password_list)
    input_password.insert(0, password_list)
    pyperclip.copy(password_list)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty entries", message="Please, make sure you haven't left any fields empty.")
    else:
        try:
            with open("passwords.json", mode="r") as passwords:
                # Reading old data
                data = json.load(passwords)
        except FileNotFoundError:
            with open("passwords.json", mode="w") as passwords:
                # Create file
                json.dump(new_data, passwords, indent=4)
        else:
            with open("passwords.json", mode="w") as passwords:
                # Updating old data with new data
                data.update(new_data)
                # Saving updated data
                json.dump(data, passwords, indent=4)
        finally:
            input_website.delete(0, "end")
            input_email.delete(0, "end")
            input_email.insert(0, "teste@gmail.com")
            input_password.delete(0, "end")

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = input_website.get()
    try:
        with open("passwords.json", mode="r") as passwords:
            # Reading old data
            data = json.load(passwords)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="No Data File Found")
    else:
        try:
            messagebox.showinfo(title=website, message=f"Website: {website}\n"
                                                       f"Email: {data[website]['email']}\n"
                                                       f"Password: {data[website]['password']}")
        except KeyError:
            messagebox.showinfo(title="ERROR", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas - Logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label - Website
website_label = Label(text="Website:", fg="black")
website_label.grid(column=0, row=1)

# Label - Email/Username
website_label = Label(text="Email/Username:", fg="black")
website_label.grid(column=0, row=2)

# Label - Password
website_label = Label(text="Password:", fg="black")
website_label.grid(column=0, row=3)

# Button - Generate Password
button_generate = Button(text="Generate Password", command=password_generator)
button_generate.grid(column=2, row=3, sticky="EW")

# Button - Add
button_add = Button(text="Add", command=save_password, width=36)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

# Button - Search
button_search = Button(text="Search", command=find_password)
button_search.grid(column=2, row=1, sticky="EW")

# Entry - Website
input_website = Entry(width=21)
input_website.grid(column=1, row=1, sticky="EW")
input_website.focus()

# Entry - Email/Username
input_email = Entry(width=35)
input_email.grid(column=1, row=2, columnspan=2, sticky="EW")
input_email.insert(0, "test@gmail.com")

# Entry - Password
input_password = Entry(width=21)
input_password.grid(column=1, row=3, sticky="EW")

window.mainloop()
