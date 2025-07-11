import tkinter as tk
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Exit", "Do you really want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Close Confirmation Demo")
root.geometry("300x200")


root.protocol("WM_DELETE_WINDOW", on_closing)

label = tk.Label(root, text="Try closing the window!", font=("Arial", 12))
label.pack(pady=60)

root.mainloop()
