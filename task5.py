import tkinter as tk


root = tk.Tk()
root.title("Fixed Size Frame")
root.geometry("400x300")  

frame = tk.Frame(root, bg="lightblue", width=200, height=100, bd=2, relief=tk.RIDGE)
frame.pack(padx=20, pady=20)


frame.pack_propagate(False)


label = tk.Label(frame, text="Fixed Size Frame", bg="lightblue")
label.pack(pady=10)


root.mainloop()
