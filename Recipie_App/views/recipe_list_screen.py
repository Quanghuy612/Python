import tkinter as tk
from tkinter import ttk

class RecipeListScreen:
    def __init__(self, root, controller):
        self.controller = controller

        # Main frame
        self.frame = tk.Frame(root, bg="#fff3e0")

        # Title
        tk.Label(self.frame, text="Recipes", font=("Helvetica", 36, "bold"),
                 bg="#fff3e0", fg="#f39c12").pack(pady=20)

        # Scrollable Canvas
        self.canvas = tk.Canvas(self.frame, bg="#fff3e0", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#fff3e0")

        # Bind scrolling
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Layout Scrollbar & Canvas
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Back Button
        tk.Button(self.frame, text="Back", font=("Helvetica", 14), bg="#e74c3c", fg="white",
                  relief="flat", command=self.controller.show_categories, padx=20, pady=10).pack(pady=10)

    def update_recipes(self, recipes):
        """Update the recipe list dynamically."""
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for recipe in recipes:
            frame = tk.Frame(self.scrollable_frame, bg="#ffffff", borderwidth=1, relief="solid")
            frame.pack(fill="x", pady=10, padx=50)

            image = self.controller.get_random_image()
            if image:
                img_label = tk.Label(frame, image=image, bg="#ffffff")
                img_label.image = image  # Prevent garbage collection
                img_label.pack(side="left", padx=10)

            tk.Label(frame, text=recipe["name"], font=("Helvetica", 16, "bold"),
                     fg="#2c3e50", bg="#ffffff", wraplength=500).pack(side="left", padx=10, pady=5)

            tk.Button(frame, text="View", font=("Helvetica", 12), bg="#f1c40f", fg="white", relief="flat",
                      command=lambda rid=recipe["id"]: self.controller.show_recipe_detail(rid),
                      padx=15, pady=5).pack(side="right", padx=10)
