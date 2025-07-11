import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("PanedWindow Example")


pane = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
pane.pack(fill=tk.BOTH, expand=True)


left_label = ttk.Label(pane, text="Left Side", background="lightblue", anchor="center")
pane.add(left_label, weight=1)


right_label = ttk.Label(pane, text="Right Side", background="lightgreen", anchor="center")
pane.add(right_label, weight=1)

root.mainloop()
