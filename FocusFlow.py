import time
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow library for images

# Set the duration for work and break periods in minutes
WORK_MINUTES = 25
SHORT_BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 15
WORK_SESSIONS_BEFORE_LONG_BREAK = 4

class PomodoroTimer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("FocusFlow - Pomodoro Timer")
        self.window.config(padx=50, pady=50, bg="white")

        # Try loading the tomato image, if not found, just show the timer without the image
        try:
            self.tomato_img = Image.open("tomato.png")
            self.tomato_img = self.tomato_img.resize((150, 150), Image.ANTIALIAS)
            self.tomato_photo = ImageTk.PhotoImage(self.tomato_img)
            self.canvas = tk.Canvas(self.window, width=200, height=224, bg="white", highlightthickness=0)
            self.canvas.create_image(100, 112, image=self.tomato_photo)
            self.canvas.pack()
        except FileNotFoundError:
            print("Tomato image not found. Running without it.")

        # Variables to keep track of sessions and time
        self.sessions_completed = 0
        self.is_working = True
        self.time_left = WORK_MINUTES * 60

        # Create labels and buttons with style
        self.label = tk.Label(self.window, text="Time to Work!", font=("Helvetica", 16), bg="white", fg="green")
        self.label.pack(pady=20)

        self.time_label = tk.Label(self.window, text=self.format_time(self.time_left), font=("Helvetica", 48), bg="white", fg="black")
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(self.window, text="Start", command=self.start_timer, font=("Helvetica", 14), bg="green", fg="white")
        self.start_button.pack(pady=20)

        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset_timer, font=("Helvetica", 14), bg="red", fg="white")
        self.reset_button.pack(pady=20)

        self.window.mainloop()

    def start_timer(self):
        if self.is_working:
            self.label.config(text="Time to Work!", fg="green")
        else:
            self.label.config(text="Take a Break!", fg="blue")

        self.window.after(1000, self.update_timer)

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=self.format_time(self.time_left))
            self.window.after(1000, self.update_timer)
        else:
            self.sessions_completed += 1
            if self.is_working:
                if self.sessions_completed % WORK_SESSIONS_BEFORE_LONG_BREAK == 0:
                    self.time_left = LONG_BREAK_MINUTES * 60
                    messagebox.showinfo("Break Time", "Time for a long break!")
                else:
                    self.time_left = SHORT_BREAK_MINUTES * 60
                    messagebox.showinfo("Break Time", "Time for a short break!")
            else:
                self.time_left = WORK_MINUTES * 60
                messagebox.showinfo("Work Time", "Back to work!")

            self.is_working = not self.is_working
            self.start_timer()

    def reset_timer(self):
        self.sessions_completed = 0
        self.is_working = True
        self.time_left = WORK_MINUTES * 60
        self.time_label.config(text=self.format_time(self.time_left))
        self.label.config(text="Time to Work!", fg="green")

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

# Run the Pomodoro Timer
PomodoroTimer()
