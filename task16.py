import tkinter as tk


root = tk.Tk()
root.title("Horizontal PanedWindow")
root.geometry("400x200")


paned = tk.PanedWindow(root, orient=tk.HORIZONTAL, sashrelief=tk.RAISED, bd=2)
paned.pack(fill="both", expand=True)

left_frame = tk.Frame(paned, bg="lightblue", width=200, height=200)
right_frame = tk.Frame(paned, bg="lightgreen", width=200, height=200)


paned.add(left_frame)
paned.add(right_frame)


tk.Label(left_frame, text="Left Frame", bg="lightblue").pack(pady=20)
tk.Label(right_frame, text="Right Frame", bg="lightgreen").pack(pady=20)


root.mainloop()
