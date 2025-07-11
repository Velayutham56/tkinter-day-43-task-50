import tkinter as tk

def open_file(filename="sample.txt"):
    print(f"Opening: {filename}")
    update_recent_files(filename)

def update_recent_files(filename):
    
    if filename not in recent_files:
        recent_files.insert(0, filename)
        if len(recent_files) > 5:
            recent_files.pop() 
    refresh_recent_menu()

def refresh_recent_menu():
    recent_menu.delete(0, tk.END)  
    for file in recent_files:
        recent_menu.add_command(label=file, command=lambda f=file: open_file(f))

root = tk.Tk()
root.title("Dynamic Menu Update")
root.geometry("300x200")

recent_files = ["project.py", "notes.txt"]  

menu_bar = tk.Menu(root)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open default", command=lambda: open_file("default.txt"))
file_menu.add_cascade(label="Recent Files", menu=tk.Menu(file_menu))  
menu_bar.add_cascade(label="File", menu=file_menu)


recent_menu = tk.Menu(file_menu, tearoff=0)
file_menu.entryconfig("Recent Files", menu=recent_menu)
refresh_recent_menu()

root.config(menu=menu_bar)
root.mainloop()
