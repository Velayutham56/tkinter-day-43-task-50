import tkinter as tk
from tkinter import messagebox

def submit_data():
    response = messagebox.askyesno("Confirm Submission", "Do you want to submit the data?")
    if response:
        messagebox.showinfo("Success", "Data submitted successfully!")
    else:
        messagebox.showwarning("Cancelled", "Data submission cancelled.")

root = tk.Tk()
root.title("Form Submission Demo")
root.geometry("300x250")


tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack(pady=5)


submit_btn = tk.Button(root, text="Submit", command=submit_data)
submit_btn.pack(pady=20)

root.mainloop()
