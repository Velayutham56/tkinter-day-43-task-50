import tkinter as tk
from tkinter import messagebox

def new_file():
    messagebox.showinfo("New", "Create a new file")

def open_file():
    messagebox.showinfo("Open", "Open an existing file")

def cut_text():
    messagebox.showinfo("Cut", "Cut selected text")

def copy_text():
    messagebox.showinfo("Copy", "Copy selected text")

def paste_text():
    messagebox.showinfo("Paste", "Paste from clipboard")

root = tk.Tk()
root.title("Menu Bar Example")
root.geometry("300x200")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)


edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_bar)
root.mainloop()
