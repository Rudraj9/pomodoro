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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="BREAK", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="WORK", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_mins = math.floor(count / 60)
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        global timer
        timer=window.after(1000, countdown,(count - 1))
    else:
        start_timer()
        marks=" "
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks="✔"
        checkmark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Start")
window.config(padx=100,pady=50, bg=YELLOW)


title_label=Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW)

canvas.create_image(100, 112)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 115, image=tomato_image)
timer_text=canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
start_button=Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button=Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2,)

checkmark=Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
checkmark.grid(column=1, row=3)

window.mainloop()
