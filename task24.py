import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Widgets in PanedWindow")
root.geometry("800x500")


outer_pane = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
outer_pane.pack(fill=tk.BOTH, expand=True)


left_frame = ttk.Frame(outer_pane, padding=10)
entry_label = ttk.Label(left_frame, text="Enter Text:")
entry_label.pack(anchor="nw")
entry_widget = ttk.Entry(left_frame, width=30)
entry_widget.pack(anchor="nw", pady=5)
outer_pane.add(left_frame, weight=2)


middle_frame = ttk.Frame(outer_pane, padding=10)
list_label = ttk.Label(middle_frame, text="Choose Item:")
list_label.pack(anchor="nw")
listbox = tk.Listbox(middle_frame)
for item in ["One", "Two", "Three", "Four"]:
    listbox.insert(tk.END, item)
listbox.pack(fill=tk.BOTH, expand=True, pady=5)
outer_pane.add(middle_frame, weight=2)


canvas = tk.Canvas(outer_pane, background="lavender")
outer_pane.add(canvas, weight=3)

root.mainloop()
