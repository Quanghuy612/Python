import tkinter as tk
from tkinter import ttk

def create_form(root, submit_callback):
    """Tạo giao diện người dùng cho form đăng ký."""
    
    # Variables to store user input
    name_var = tk.StringVar()
    email_var = tk.StringVar()
    password_var = tk.StringVar()

    # Create a frame container
    frame = tk.Frame(root, padx=10, pady=10, bg="white", relief=tk.RIDGE, bd=2)
    frame.pack(pady=20)

    # Title
    title = tk.Label(frame, text="Đăng Ký Người Dùng", font=("Arial", 16, "bold"), bg="white", fg="#333")
    title.grid(row=0, column=0, columnspan=2, pady=10)

    # Name Label & Entry
    tk.Label(frame, text="Tên:", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky=tk.W, pady=5)
    entry_name = tk.Entry(frame, textvariable=name_var, font=("Arial", 12), width=25)
    entry_name.grid(row=1, column=1, pady=5)
    add_placeholder(entry_name, "Nhập tên của bạn")

    # Email Label & Entry
    tk.Label(frame, text="Email:", font=("Arial", 12), bg="white").grid(row=2, column=0, sticky=tk.W, pady=5)
    entry_email = tk.Entry(frame, textvariable=email_var, font=("Arial", 12), width=25)
    entry_email.grid(row=2, column=1, pady=5)
    add_placeholder(entry_email, "Nhập email của bạn")

    # Password Label & Entry
    tk.Label(frame, text="Mật khẩu:", font=("Arial", 12), bg="white").grid(row=3, column=0, sticky=tk.W, pady=5)
    entry_password = tk.Entry(frame, textvariable=password_var, font=("Arial", 12), width=25, show="*")
    entry_password.grid(row=3, column=1, pady=5)

    # Submit Button
    submit_btn = ttk.Button(frame, text="Đăng Ký", command=lambda: submit_callback(name_var, email_var, password_var))
    submit_btn.grid(row=4, column=0, columnspan=2, pady=10)

    return name_var, email_var, password_var, submit_btn

# Function to add placeholders to Entry fields
def add_placeholder(entry, text):
    entry.insert(0, text)
    entry.config(fg="grey")

    def on_focus_in(event):
        if entry.get() == text:
            entry.delete(0, "end")
            entry.config(fg="black")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, text)
            entry.config(fg="grey")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
