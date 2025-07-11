import tkinter as tk


root = tk.Tk()
root.title("Styled Frame")
root.geometry("300x200")


styled_frame = tk.Frame(root, bg="lightblue", borderwidth=5, relief="ridge")
styled_frame.pack(padx=20, pady=20, fill="both", expand=True)


tk.Label(styled_frame, text="Styled Frame Content", bg="lightblue").pack(pady=10)


root.mainloop()
