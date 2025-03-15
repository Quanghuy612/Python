import tkinter as tk
from layout import create_layout

def run_movie_app():
    """Launch the movie app"""
    root = tk.Tk()
    create_layout(root)
    root.mainloop()

if __name__ == "__main__":
    run_movie_app()
