import tkinter as tk
from tkinter import messagebox

def confirm_action():
    response = messagebox.askquestion("Confirmation", "Do you want to proceed?")
    if response == "yes":
        print("User chose Yes")
    else:
        print("User chose No")

root = tk.Tk()
root.title("Ask Question Demo")
root.geometry("300x200")

btn = tk.Button(root, text="Ask Me!", command=confirm_action)
btn.pack(pady=50)

root.mainloop()
