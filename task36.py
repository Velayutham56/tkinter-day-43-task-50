import tkinter as tk

def new_file():
    print("New file clicked")

def open_file():
    print("Open file clicked")

def save_file():
    print("Save file clicked")

root = tk.Tk()
root.title("Toolbar Example")
root.geometry("400x300")


toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)


new_btn = tk.Button(toolbar, text="New", command=new_file)
new_btn.pack(side=tk.LEFT, padx=2, pady=2)

open_btn = tk.Button(toolbar, text="Open", command=open_file)
open_btn.pack(side=tk.LEFT, padx=2, pady=2)

save_btn = tk.Button(toolbar, text="Save", command=save_file)
save_btn.pack(side=tk.LEFT, padx=2, pady=2)


toolbar.pack(side=tk.TOP, fill=tk.X)


text_area = tk.Text(root)
text_area.pack(fill=tk.BOTH, expand=True)

root.mainloop()
