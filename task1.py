import tkinter as tk


root = tk.Tk()
root.title("Frame with Label")
root.geometry("300x150")


frame = tk.Frame(root, bg="lightblue", bd=2, relief=tk.RIDGE)
frame.pack(padx=20, pady=20, fill="both", expand=True)


label = tk.Label(frame, text="Hello from inside the Frame!", bg="lightblue", font=("Arial", 12))
label.pack(pady=10)

root.mainloop()
