import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Three Pane Layout with Nested PanedWindows")
root.geometry("800x500")


outer_pane = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
outer_pane.pack(fill=tk.BOTH, expand=True)


left_label = ttk.Label(outer_pane, text="Left Pane", background="lightblue", anchor="center")
outer_pane.add(left_label, weight=1)


nested_pane = ttk.PanedWindow(outer_pane, orient=tk.VERTICAL)


middle_label = ttk.Label(nested_pane, text="Middle Pane", background="lightgreen", anchor="center")
nested_pane.add(middle_label, weight=2)


right_label = ttk.Label(nested_pane, text="Right Pane", background="lightyellow", anchor="center")
nested_pane.add(right_label, weight=2)


outer_pane.add(nested_pane, weight=3)

root.mainloop()
