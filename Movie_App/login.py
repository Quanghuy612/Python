import tkinter as tk
from tkinter import messagebox
from db import verify_user
import main  # Import main, but it won't run automatically now

def attempt_login(username_entry, password_entry, root):
    """Verify user credentials and redirect to movie app if successful"""
    username = username_entry.get()
    password = password_entry.get()

    if verify_user(username, password):  # Check MongoDB
        messagebox.showinfo("Login Successful", "Welcome to the Movie App!")
        root.destroy()  # Close login window
        open_movie_app()  # Open the movie app
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_movie_app():
    """Launch the movie app from main.py"""
    main.run_movie_app()

def create_login_window():
    """Create the Tkinter login window"""
    root = tk.Tk()
    root.title("Login")
    root.geometry("400x300")
    root.configure(bg="#121212")

    tk.Label(root, text="Username:", font=("Arial", 14), fg="white", bg="#121212").pack(pady=5)
    username_entry = tk.Entry(root, font=("Arial", 14), width=30)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password:", font=("Arial", 14), fg="white", bg="#121212").pack(pady=5)
    password_entry = tk.Entry(root, font=("Arial", 14), width=30, show="*")  # Hide password
    password_entry.pack(pady=5)

    login_button = tk.Button(root, text="Login", font=("Arial", 14), bg="#E50914", fg="white",
                             command=lambda: attempt_login(username_entry, password_entry, root))
    login_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_login_window()
