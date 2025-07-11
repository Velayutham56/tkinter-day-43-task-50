import tkinter as tk
from tkinter import messagebox

def open_name_dialog():
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
            messagebox.showinfo("Name Received", f"Hello, {name}!")
            dialog.destroy()
        else:
            messagebox.showwarning("Empty Input", "Name cannot be empty.")

    def cancel():
        dialog.destroy()

    button_frame = tk.Frame(dialog)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Submit", command=submit_name).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Cancel", command=cancel).pack(side=tk.LEFT, padx=5)

root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

tk.Button(root, text="Enter Name", command=open_name_dialog).pack(pady=60)

root.mainloop()
