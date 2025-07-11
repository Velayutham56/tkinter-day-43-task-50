import tkinter as tk

root = tk.Tk()
root.title("Horizontal Buttons Toolbar")
root.geometry("400x300")


toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)


btn_open = tk.Button(toolbar, text="Open")
btn_open.pack(side=tk.LEFT, padx=2, pady=2)

btn_save = tk.Button(toolbar, text="Save")
btn_save.pack(side=tk.LEFT, padx=2, pady=2)

btn_exit = tk.Button(toolbar, text="Exit")
btn_exit.pack(side=tk.LEFT, padx=2, pady=2)


toolbar.pack(side=tk.TOP, fill=tk.X)


text_area = tk.Text(root)
text_area.pack(fill=tk.BOTH, expand=True)

root.mainloop()
