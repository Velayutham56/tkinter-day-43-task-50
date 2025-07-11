import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Scrollable Text in PanedWindow")


pane = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
pane.pack(fill=tk.BOTH, expand=True)


left_label = ttk.Label(pane, text="Left Pane", background="lightblue", anchor="center")
pane.add(left_label, weight=1)


text_frame = ttk.Frame(pane)


scrollbar = ttk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


text_widget = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


scrollbar.config(command=text_widget.yview)


pane.add(text_frame, weight=3)

root.mainloop()

