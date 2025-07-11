import tkinter as tk


root = tk.Tk()
root.title("Login Form")
root.geometry("300x180")


login_frame = tk.Frame(root, bg="lightgray", bd=2, relief="ridge")
login_frame.pack(padx=20, pady=20, fill="both", expand=True)


tk.Label(login_frame, text="Username:", bg="lightgray").grid(row=0, column=0, padx=5, pady=5, sticky="e")
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)


tk.Label(login_frame, text="Password:", bg="lightgray").grid(row=1, column=0, padx=5, pady=5, sticky="e")
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)


tk.Button(login_frame, text="Login").grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()
