import tkinter as tk
from tkinter import messagebox

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message!")

root = tk.Tk()
root.title("Warning Button Demo")
root.geometry("300x200")

btn = tk.Button(root, text="Show Warning", command=show_warning)
btn.pack(pady=50)

root.mainloop()
