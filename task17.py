import tkinter as tk


root = tk.Tk()
root.title("Vertical PanedWindow Example")
root.geometry("400x300")


paned = tk.PanedWindow(root, orient=tk.VERTICAL, sashrelief=tk.RAISED, bd=2)
paned.pack(fill="both", expand=True)


text_frame = tk.Frame(paned, bg="white")
text_area = tk.Text(text_frame, height=8, wrap="word")
text_area.pack(fill="both", expand=True, padx=5, pady=5)
paned.add(text_frame)


form_frame = tk.Frame(paned, bg="lightgray")
tk.Label(form_frame, text="Name:", bg="lightgray").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Email:", bg="lightgray").grid(row=1, column=0, padx=5, pady=5, sticky="e")
email_entry = tk.Entry(form_frame)
email_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(form_frame, text="Submit").grid(row=2, column=0, columnspan=2, pady=10)
paned.add(form_frame)


root.mainloop()
