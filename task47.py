import tkinter as tk
from tkinter import messagebox

def open_name_dialog(callback):
    dialog = tk.Toplevel(root)
    dialog.title("Enter Your Name")
    dialog.geometry("300x150")
    dialog.grab_set()

    tk.Label(dialog, text="Please enter your name:").pack(pady=10)
    name_var = tk.StringVar()
    name_entry = tk.Entry(dialog, textvariable=name_var)
    name_entry.pack(pady=5)

    def submit_name():
        name = name_var.get().strip()
        if name:
            callback(name)  
            dialog.destroy()
        else:
            messagebox.showwarning("Empty Input", "Name cannot be empty.")

    def cancel():
        dialog.destroy()

    tk.Button(dialog, text="Submit", command=submit_name).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(dialog, text="Cancel", command=cancel).pack(side=tk.RIGHT, padx=10, pady=10)

def receive_name(name):
    
    name_label.config(text=f"Welcome, {name}!")

root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

tk.Button(root, text="Enter Name", command=lambda: open_name_dialog(receive_name)).pack(pady=20)

name_label = tk.Label(root, text="No name entered yet.")
name_label.pack(pady=20)

root.mainloop()
