import tkinter as tk
from tkinter import ttk
import os

root = tk.Tk()
root.title("File Explorer Pane")
root.geometry("800x500")


pane = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
pane.pack(fill=tk.BOTH, expand=True)


explorer_frame = ttk.Frame(pane)
file_tree = ttk.Treeview(explorer_frame)
file_tree.pack(fill=tk.BOTH, expand=True)


tree_scroll = ttk.Scrollbar(explorer_frame, orient=tk.VERTICAL, command=file_tree.yview)
file_tree.configure(yscrollcommand=tree_scroll.set)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

pane.add(explorer_frame, weight=2)


def populate_tree(parent, path):
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            node = file_tree.insert(parent, "end", text=item, open=False)
            if os.path.isdir(full_path):
                file_tree.insert(node, "end")  # Placeholder for expanding
    except PermissionError:
        pass

def on_open(event):
    node = file_tree.focus()
    path = get_full_path(node)
    if os.path.isdir(path) and not file_tree.get_children(node):
        populate_tree(node, path)

def get_full_path(item):
    parts = []
    while item:
        parts.insert(0, file_tree.item(item, "text"))
        item = file_tree.parent(item)
    return os.path.join(os.getcwd(), *parts)

file_tree.bind("<<TreeviewOpen>>", on_open)
populate_tree("", os.getcwd())

canvas = tk.Canvas(pane, background="white")
pane.add(canvas, weight=4)

root.mainloop()
