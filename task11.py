import tkinter as tk


root = tk.Tk()
root.title("Pack and Grid in Separate Frames")
root.geometry("400x250")


pack_frame = tk.Frame(root, bg="lightblue", bd=2, relief="ridge")
pack_frame.pack(side="top", fill="x", padx=10, pady=10)

tk.Label(pack_frame, text="Packed Label", bg="lightblue").pack(pady=5)
tk.Button(pack_frame, text="Packed Button").pack(pady=5)


grid_frame = tk.Frame(root, bg="lightgreen", bd=2, relief="groove")
grid_frame.pack(side="bottom", fill="x", padx=10, pady=10)

tk.Label(grid_frame, text="Grid Label", bg="lightgreen").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(grid_frame).grid(row=0, column=1, padx=5, pady=5)
tk.Button(grid_frame, text="Grid Button").grid(row=1, column=0, columnspan=2, pady=10)


root.mainloop()
