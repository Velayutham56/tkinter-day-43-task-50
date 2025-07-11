import tkinter as tk


root = tk.Tk()
root.title("Left Sidebar Navigation")
root.geometry("400x300")

sidebar = tk.Frame(root, bg="lightgray", width=120)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False) 


btn_home = tk.Button(sidebar, text="Home")
btn_home.pack(pady=10, fill="x")

btn_profile = tk.Button(sidebar, text="Profile")
btn_profile.pack(pady=10, fill="x")

btn_settings = tk.Button(sidebar, text="Settings")
btn_settings.pack(pady=10, fill="x")


content = tk.Frame(root, bg="white")
content.pack(side="left", fill="both", expand=True)
tk.Label(content, text="Main Content Area", bg="white", font=("Arial", 14)).pack(pady=20)


root.mainloop()
