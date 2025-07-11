import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Resizable Canvas with PanedWindow")


pane = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
pane.pack(fill=tk.BOTH, expand=True)


left_label = ttk.Label(pane, text="Tools", background="lightgray", anchor="center")
pane.add(left_label, weight=1)


canvas = tk.Canvas(pane, background="white")
pane.add(canvas, weight=4)


def on_resize(event):
    canvas.config(width=event.width, height=event.height)

canvas.bind("<Configure>", on_resize)

root.mainloop()
