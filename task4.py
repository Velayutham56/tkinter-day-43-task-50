import tkinter as tk


root = tk.Tk()
root.title("Nested Frames Example")
root.geometry("300x200")


outer_frame = tk.Frame(root, bg="lightblue", bd=2, relief=tk.RIDGE)
outer_frame.pack(padx=10, pady=10, fill="both", expand=True)

inner_frame = tk.Frame(outer_frame, bg="lightgreen", bd=2, relief=tk.SUNKEN)
inner_frame.pack(padx=10, pady=10, fill="both", expand=True)


label = tk.Label(inner_frame, text="I'm inside the inner frame!", bg="lightgreen")
label.pack(pady=10)


root.mainloop()
