import tkinter as tk
from tkinter import messagebox

def new_file(event=None):
    print("New file created")

def open_file(event=None):
    print("Opening file...")

def save_file(event=None):
    print("File saved")

def exit_app(event=None):
    root.quit()

def show_about(event=None):
    messagebox.showinfo("About", "Made with ❤️ using Tkinter\nDeveloper: Velayutham")

root = tk.Tk()
root.title("Shortcut Menu Example")
root.geometry("300x200")

menu_bar = tk.Menu(root)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app, accelerator="Ctrl+Q")
menu_bar.add_cascade(label="File", menu=file_menu)


help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about, accelerator="Ctrl+H")
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)


root.bind_all("<Control-n>", new_file)
root.bind_all("<Control-o>", open_file)
root.bind_all("<Control-s>", save_file)
root.bind_all("<Control-q>", exit_app)
root.bind_all("<Control-h>", show_about)

root.mainloop()
