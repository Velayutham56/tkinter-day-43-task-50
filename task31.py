import tkinter as tk

def new_file():
    print("New file created")

def open_file():
    print("Opening file...")

def save_file():
    print("File saved")

def exit_app():
    root.quit()

root = tk.Tk()
root.title("Multiple Submenus Example")
root.geometry("300x200")

menu_bar = tk.Menu(root)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)


menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()
