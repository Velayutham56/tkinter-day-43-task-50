import tkinter as tk

def open_centered_dialog():
    dialog = tk.Toplevel(root)
    dialog.title("Centered Dialog")

    
    dialog_width = 300
    dialog_height = 150

   
    screen_width = dialog.winfo_screenwidth()
    screen_height = dialog.winfo_screenheight()

   
    x = (screen_width // 2) - (dialog_width // 2)
    y = (screen_height // 2) - (dialog_height // 2)

    
    dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

    dialog.grab_set()  

    tk.Label(dialog, text="Centered with geometry()").pack(pady=40)

root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

tk.Button(root, text="Open Centered Dialog", command=open_centered_dialog).pack(pady=60)

root.mainloop()
