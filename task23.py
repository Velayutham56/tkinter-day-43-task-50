import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Pane Background Colors")
root.geometry("600x400")


pane = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
pane.pack(fill=tk.BOTH, expand=True)


left_frame = tk.Frame(pane, background="lightcoral")
left_label = ttk.Label(left_frame, text="Left Pane", background="lightcoral", anchor="center")
left_label.pack(expand=True)
pane.add(left_frame, weight=1)


right_frame = tk.Frame(pane, background="paleturquoise")
right_label = ttk.Label(right_frame, text="Right Pane", background="paleturquoise", anchor="center")
right_label.pack(expand=True)
pane.add(right_frame, weight=2)

root.mainloop()
