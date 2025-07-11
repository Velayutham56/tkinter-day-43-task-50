import tkinter as tk
from tkinter import messagebox

def new_file():
    print("New file created")

def open_file():
    print("Opening file...")

def exit_app():
    root.quit()

def cut_text():
    print("Cut")

def copy_text():
    print("Copy")

def paste_text():
    print("Paste")

def show_about():
    messagebox.showinfo("About", "This app was made with ❤️ using Tkinter.\nDeveloper: Velayutham")

root = tk.Tk()
root.title("Menu Bar with Help Menu")
root.geometry("300x200")

menu_bar = tk.Menu(root)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_separator()
edit_menu.add_command(label="Paste", command=paste_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)
root.mainloop()
