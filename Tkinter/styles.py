from tkinter import ttk

def apply_styles(submit_btn):
    """Áp dụng kiểu cho nút."""
    
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), padding=5)
    style.configure("Hover.TButton", font=("Arial", 12), padding=5, background="lightblue")

    def on_enter(e):
        submit_btn.config(style="Hover.TButton")

    def on_leave(e):
        submit_btn.config(style="TButton")

    submit_btn.bind("<Enter>", on_enter)
    submit_btn.bind("<Leave>", on_leave)
