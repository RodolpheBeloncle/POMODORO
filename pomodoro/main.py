from tkinter import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 3
LONG_BREAK_MIN = 4
reps = 0
timer = None




# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_title.config(text="Timer")
    check_marks.config(text="")
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
        count_down(long_break_sec)
        timer_title.config(text="Long Break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_title.config(text="Short Break",fg=PINK)


    else:
        count_down(work_sec)
        timer_title.config(text="Focus Time",fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # func call itself + modulo way to keep formatted counter
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        #canvas.itemconfig(timer_text, text=f"{'{:02d}'.format(floor(count/60))}:{'{:02d}'.format(count % 60)}")

    else:
        start_timer()
        # CheckMark
        working_session = floor(reps / 2)
        checked = ""
        # each session every 2 rep = 0 or 1
        for _ in range(working_session):
            checked += "✓"
            check_marks.config(text=checked,bg=YELLOW)








# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

# Timer set
timer_title = Label(text="Timer",font=("Abadi MT Condensed Extra Bold",35,"bold"),fg=GREEN,highlightthickness=0,bg=YELLOW)
timer_title.grid(column=2,row=1)

# Canvas img
canvas = Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,110,image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2,row=2)


# Set button start & reset
start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=1,row=3)
reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=3,row=3)

# create check mark:

check_marks = Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=2, row=3)


window.mainloop()

