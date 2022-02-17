from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
check_count = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    if reps == 2 or reps == 4 or reps == 6:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    if reps == 8:
        timer_label.config(text="Long Brake", fg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global check_count
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        global reps
        if reps == 1 or reps == 3 or reps == 5 or reps == 7:
            check_count += 1
            check_label.config(text="✔" * check_count)
        reps += 1
        if reps > 8:
            reps = 1
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Label - Timer
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(column=1, row=0)
timer_label.config(padx=10, pady=10)

# Label - check
check_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check_label.grid(column=1, row=3)

# Button - Start
button = Button(text="Start", command=start_timer)
button.grid(column=0, row=2)

# Button - Reset
button = Button(text="Reset", command=reset_timer)
button.grid(column=2, row=2)

window.mainloop()
