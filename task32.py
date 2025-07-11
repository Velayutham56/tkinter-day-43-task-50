import tkinter as tk

root = tk.Tk()
root.title("Menu Cascade Demo")
root.geometry("300x200")


menu_bar = tk.Menu(root)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


menu_bar.add_cascade(label="File", menu=file_menu)


edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")


menu_bar.add_cascade(label="Edit", menu=edit_menu)


root.config(menu=menu_bar)
root.mainloop()
