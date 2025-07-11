import tkinter as tk


root = tk.Tk()
root.title("Horizontal Frame Alignment")
root.geometry("400x150")


frame1 = tk.Frame(root, bg="lightblue", width=100, height=100)
frame1.pack(side="left", padx=10, pady=10)
frame1.pack_propagate(False)
tk.Label(frame1, text="Frame 1", bg="lightblue").pack()


frame2 = tk.Frame(root, bg="lightgreen", width=100, height=100)
frame2.pack(side="left", padx=10, pady=10)
frame2.pack_propagate(False)
tk.Label(frame2, text="Frame 2", bg="lightgreen").pack()


frame3 = tk.Frame(root, bg="lightcoral", width=100, height=100)
frame3.pack(side="left", padx=10, pady=10)
frame3.pack_propagate(False)
tk.Label(frame3, text="Frame 3", bg="lightcoral").pack()


root.mainloop()
