import tkinter as tk
from datetime import datetime

def update_time():
    now = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=now)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Current Time")

time_label = tk.Label(root, font=("Arial", 48))
time_label.pack(pady=30)

update_time()
root.mainloop()
