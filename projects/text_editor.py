import tkinter as tk
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w") as f:
            f.write(textbox.get("1.0", tk.END))

def open_file():
    file = filedialog.askopenfilename()
    if file:
        with open(file, "r") as f:
            content = f.read()
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, content)

root = tk.Tk()
root.title("Simple Text Editor")

textbox = tk.Text(root, wrap="word", width=60, height=20)
textbox.pack(padx=10, pady=10)

root.mainloop()
