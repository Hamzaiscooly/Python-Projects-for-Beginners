import tkinter as tk

def double_number():
    try:
        num = int(entry.get())
        result_label.config(text=f"Result: {num * 2}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

root = tk.Tk()
root.title("Number Doubler")

tk.Label(root, text="Enter a number:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Double It!", command=double_number).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
