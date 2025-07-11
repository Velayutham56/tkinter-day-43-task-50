import tkinter as tk


root = tk.Tk()
root.title("Header, Content, Footer Layout")
root.geometry("400x300")


header = tk.Frame(root, bg="skyblue", height=50)
header.pack(fill="x")
tk.Label(header, text="Header", bg="skyblue", font=("Arial", 14)).pack(pady=10)


content = tk.Frame(root, bg="white")
content.pack(fill="both", expand=True)
tk.Label(content, text="Main Content Area", bg="white", font=("Arial", 12)).pack(pady=20)


footer = tk.Frame(root, bg="lightgray", height=40)
footer.pack(fill="x")
tk.Label(footer, text="Footer", bg="lightgray").pack(pady=5)


header.pack_propagate(False)
footer.pack_propagate(False)


root.mainloop()
