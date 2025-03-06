import tkinter as tk
from tkinter import ttk
from ui import create_form  # Import function from ui.py
from styles import apply_styles  # Import function from styles.py

def submit(name_var, email_var, password_var):
    print(f"Tên: {name_var.get()}, Email: {email_var.get()}, Mật khẩu: {password_var.get()}")

# Create main window
root = tk.Tk()
root.title("Form Đăng Ký Người Dùng")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Set background color
root.configure(bg="#e6f7ff")

# Create form
name_var, email_var, password_var, submit_btn = create_form(root, submit)

# Apply styles
apply_styles(submit_btn)

# Run the Tkinter event loop
root.mainloop()
