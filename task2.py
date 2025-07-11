import tkinter as tk


root = tk.Tk()
root.title("Three Buttons in a Frame")
root.geometry("300x200")


frame = tk.Frame(root, bg="lightgray", bd=2, relief=tk.RIDGE)
frame.pack(padx=20, pady=20, fill="both", expand=True)


btn1 = tk.Button(frame, text="Button 1")
btn1.pack(pady=5)

btn2 = tk.Button(frame, text="Button 2")
btn2.pack(pady=5)

btn3 = tk.Button(frame, text="Button 3")
btn3.pack(pady=5)


root.mainloop()
