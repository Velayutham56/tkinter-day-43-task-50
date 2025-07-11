import tkinter as tk

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

root = tk.Tk()
root.title("Menu Bar with Separators")
root.geometry("300x200")

menu_bar = tk.Menu(root)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()  # 🔻 Separator here
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_separator()  
edit_menu.add_command(label="Paste", command=paste_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_bar)
root.mainloop()
