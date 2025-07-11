import tkinter as tk
from tkinter import messagebox
import re

def open_email_dialog():
    dialog = tk.Toplevel(root)
    dialog.title("Enter Your Email")
    dialog.geometry("350x160")
    dialog.grab_set()

    tk.Label(dialog, text="Please enter your email:").pack(pady=10)
    email_var = tk.StringVar()
    tk.Entry(dialog, textvariable=email_var, width=30).pack(pady=5)

    def validate_email(email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email)

    def submit_email():
        email = email_var.get().strip()
        if validate_email(email):
            messagebox.showinfo("Valid Email", f"Email accepted: {email}")
            dialog.destroy()
        else:
            messagebox.showwarning("Invalid Email", "Please enter a valid email address.")

    def cancel():
        dialog.destroy()

    btn_frame = tk.Frame(dialog)
    btn_frame.pack(pady=15)

    tk.Button(btn_frame, text="Submit", width=10, command=submit_email).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Cancel", width=10, command=cancel).pack(side=tk.RIGHT, padx=5)

root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

tk.Button(root, text="Enter Email", command=open_email_dialog).pack(pady=60)

root.mainloop()
