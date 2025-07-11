import tkinter as tk


root = tk.Tk()
root.title("Form and Result Display")
root.geometry("400x200")


form_frame = tk.Frame(root, bg="lightyellow", bd=2, relief="groove")
form_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)


result_frame = tk.Frame(root, bg="lightblue", bd=2, relief="ridge")
result_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

tk.Label(form_frame, text="Enter your name:", bg="lightyellow").pack(pady=5)
name_entry = tk.Entry(form_frame)
name_entry.pack(pady=5)

def show_result():
    name = name_entry.get()
    result_label.config(text=f"Hello, {name}!")

tk.Button(form_frame, text="Submit", command=show_result).pack(pady=10)


result_label = tk.Label(result_frame, text="Result will appear here", bg="lightblue", font=("Arial", 12))
result_label.pack(pady=20)


root.mainloop()
