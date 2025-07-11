import tkinter as tk


root = tk.Tk()
root.title("pack_propagate Test")
root.geometry("400x300")


frame = tk.Frame(root, width=200, height=100, bg="lightblue", bd=2, relief=tk.RIDGE)
frame.pack(padx=20, pady=20)


frame.pack_propagate(False)


label = tk.Label(frame, text="This label won't resize the frame", bg="lightblue")
label.pack()


root.mainloop()
