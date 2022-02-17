from tkinter import Tk, Canvas, PhotoImage, Button, Label
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
to_learn = {}
try:
    data_words = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data_words.to_dict(orient="records")

card = None

def next_card():
    global card
    global timer
    timer = window.after(3000, turn_card)
    card = random.choice(to_learn)

    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(label_title, text="French", fill="black")
    canvas.itemconfig(label_word, text=card["French"], fill="black")



def turn_card():
    global card
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(label_title, text="English", fill="white")
    canvas.itemconfig(label_word, text=card["English"], fill="white")


def correct():
    global timer
    window.after_cancel(timer)
    next_card()
    to_learn.remove(card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")



def fail():
    global timer
    window.after_cancel(timer)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer = window.after(3000, turn_card)

# # Canvas - Card Back
# canvas_card_back = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas_card_back.create_image(400, 263, image=card_back_img)
# canvas_card_back.grid(column=0, row=0, columnspan=2, sticky="EW")

# Canvas - Card Front
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
label_title = canvas.create_text(400, 150, text="", font=TITLE_FONT)
label_word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2, sticky="EW")

# Button - Right
right_img = PhotoImage(file="./images/right.png")
button_right = Button(image=right_img, command=correct, highlightthickness=0)
button_right.grid(column=1, row=1)

# Button - Wrong
wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_img, command=fail, highlightthickness=0)
button_wrong.grid(column=0, row=1)


window.mainloop()
