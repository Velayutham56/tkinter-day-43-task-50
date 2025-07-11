import tkinter as tk

def toggle_toolbar():
    global toolbar_visible
    if toolbar_visible:
        toolbar.pack_forget()
        toggle_btn.config(text="Show Toolbar")
    else:
        toolbar.pack(side=tk.TOP, fill=tk.X)
        toggle_btn.config(text="Hide Toolbar")
    toolbar_visible = not toolbar_visible

def open_file():
    print("Open clicked")

def save_file():
    print("Save clicked")

def exit_app():
    root.quit()

root = tk.Tk()
root.title("Toolbar Toggle Example")
root.geometry("400x300")

toolbar_visible = True  


toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)

btn_open = tk.Button(toolbar, text="Open", command=open_file)
btn_open.pack(side=tk.LEFT, padx=2, pady=2)

btn_save = tk.Button(toolbar, text="Save", command=save_file)
btn_save.pack(side=tk.LEFT, padx=2, pady=2)

btn_exit = tk.Button(toolbar, text="Exit", command=exit_app)
btn_exit.pack(side=tk.LEFT, padx=2, pady=2)

toolbar.pack(side=tk.TOP, fill=tk.X)


toggle_btn = tk.Button(root, text="Hide Toolbar", command=toggle_toolbar)
toggle_btn.pack(pady=5)


text_area = tk.Text(root)
text_area.pack(fill=tk.BOTH, expand=True)

root.mainloop()
