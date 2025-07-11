import tkinter as tk
from tkinter import messagebox

def open_file():
    print("🗂️ Open file clicked")

def save_file():
    print("💾 Save file clicked")

def exit_app():
    should_exit = messagebox.askyesno("Exit", "Are you sure you want to quit?")
    if should_exit:
        root.quit()

def help_dialog():
    messagebox.showinfo("Help", "This app was built by Velayutham using Tkinter!")

root = tk.Tk()
root.title("Toolbar with Action Buttons")
root.geometry("400x300")


toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)


btn_open = tk.Button(toolbar, text="Open", command=open_file)
btn_open.pack(side=tk.LEFT, padx=2, pady=2)

btn_save = tk.Button(toolbar, text="Save", command=save_file)
btn_save.pack(side=tk.LEFT, padx=2, pady=2)

btn_help = tk.Button(toolbar, text="Help", command=help_dialog)
btn_help.pack(side=tk.LEFT, padx=2, pady=2)

btn_exit = tk.Button(toolbar, text="Exit", command=exit_app)
btn_exit.pack(side=tk.LEFT, padx=2, pady=2)


toolbar.pack(side=tk.TOP, fill=tk.X)


text_area = tk.Text(root)
text_area.pack(fill=tk.BOTH, expand=True)

root.mainloop()
