import tkinter as tk


root = tk.Tk()
root.title("Place Frame Example")
root.geometry("400x300")


frame = tk.Frame(root, width=200, height=100, bg="lightblue", bd=2, relief="ridge")
frame.place(x=50, y=80)

tk.Label(frame, text="I'm placed at (50, 80)", bg="lightblue").pack(pady=20)


root.mainloop()
