import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("Info", "This is an info message!")

root = tk.Tk()
root.title("Info Box Demo")
root.geometry("300x200")

btn = tk.Button(root, text="Show Info", command=show_info)
btn.pack(pady=50)

root.mainloop()
