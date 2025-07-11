import tkinter as tk

root = tk.Tk()
root.title("Cascade Menu Example")
root.geometry("300x200")


menu_bar = tk.Menu(root)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Attach submenu to main menu using add_cascade()
menu_bar.add_cascade(label="File", menu=file_menu)

# Add more submenus if needed
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
menu_bar.add_cascade(label="Edit", menu=edit_menu)


root.config(menu=menu_bar)

root.mainloop()
