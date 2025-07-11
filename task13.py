import tkinter as tk


root = tk.Tk()
root.title("Grouped Sections Example")
root.geometry("400x300")


personal_frame = tk.LabelFrame(root, text="Personal Info", padx=10, pady=10, bg="lightyellow")
personal_frame.pack(fill="x", padx=10, pady=10)

tk.Label(personal_frame, text="First Name:", bg="lightyellow").grid(row=0, column=0, sticky="w")
tk.Entry(personal_frame).grid(row=0, column=1)

tk.Label(personal_frame, text="Last Name:", bg="lightyellow").grid(row=1, column=0, sticky="w")
tk.Entry(personal_frame).grid(row=1, column=1)


contact_frame = tk.LabelFrame(root, text="Contact Info", padx=10, pady=10, bg="lightblue")
contact_frame.pack(fill="x", padx=10, pady=10)

tk.Label(contact_frame, text="Email:", bg="lightblue").grid(row=0, column=0, sticky="w")
tk.Entry(contact_frame).grid(row=0, column=1)

tk.Label(contact_frame, text="Phone:", bg="lightblue").grid(row=1, column=0, sticky="w")
tk.Entry(contact_frame).grid(row=1, column=1)


root.mainloop()
