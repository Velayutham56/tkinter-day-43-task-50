import tkinter as tk


root = tk.Tk()
root.title("Grid Layout Example")
root.geometry("300x150")


frame = tk.Frame(root, bg="lightyellow", bd=2, relief=tk.GROOVE)
frame.pack(padx=20, pady=20)


label = tk.Label(frame, text="Enter your name:")
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame)
entry.grid(row=0, column=1, padx=5, pady=5)

button = tk.Button(frame, text="Submit")
button.grid(row=1, column=0, columnspan=2, pady=10)


root.mainloop()
