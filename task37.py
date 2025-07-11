import tkinter as tk

def open_file():
    print("Open button clicked")

def save_file():
    print("Save button clicked")

root = tk.Tk()
root.title("Toolbar with Buttons")
root.geometry("400x300")


toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)


open_btn = tk.Button(toolbar, text="Open", command=open_file)
open_btn.pack(side=tk.LEFT, padx=2, pady=2)

save_btn = tk.Button(toolbar, text="Save", command=save_file)
save_btn.pack(side=tk.LEFT, padx=2, pady=2)

toolbar.pack(side=tk.TOP, fill=tk.X)


text_area = tk.Text(root)
text_area.pack(fill=tk.BOTH, expand=True)

root.mainloop()
