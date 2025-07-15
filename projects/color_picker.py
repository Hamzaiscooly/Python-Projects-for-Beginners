import tkinter as tk
from tkinter import colorchooser

def pick_color():
    color = colorchooser.askcolor(title="Pick a Color")[1]
    if color:
        color_label.config(text=color, bg=color)

root = tk.Tk()
root.title("Color Picker")

tk.Button(root, text="Choose Color", command=pick_color).pack(pady=10)
color_label = tk.Label(root, text="Your color will appear here!", width=30, height=2)
color_label.pack(pady=10)

root.mainloop()
