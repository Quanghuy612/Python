import tkinter as tk
from tkinter import scrolledtext, messagebox

class RecipeDetailScreen:
    def __init__(self, root, controller):
        self.controller = controller

        # Main frame
        self.frame = tk.Frame(root, bg="#fff3e0")

        # Scrollable Canvas
        self.canvas = tk.Canvas(self.frame, bg="#fff3e0", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#fff3e0")

        # Bind scrolling
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Layout Scrollbar & Canvas
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Recipe Title
        self.detail_name = tk.Label(self.scrollable_frame, font=("Helvetica", 28, "bold"), bg="#fff3e0", fg="#f39c12")
        self.detail_name.pack(pady=20)

        # Recipe Image
        self.detail_image = tk.Label(self.scrollable_frame, bg="#fff3e0", borderwidth=2, relief="solid")
        self.detail_image.pack(pady=10)

        # Info Frame (Time & Servings)
        self.detail_info_frame = tk.Frame(self.scrollable_frame, bg="#fff3e0")
        self.detail_info_frame.pack(pady=10, padx=50)

        tk.Label(self.detail_info_frame, text="Time:", font=("Helvetica", 14), fg="#2c3e50", bg="#fff3e0").pack(side="left")
        self.detail_time = tk.Label(self.detail_info_frame, font=("Helvetica", 14), fg="#2c3e50", bg="#fff3e0")
        self.detail_time.pack(side="left", padx=5)

        tk.Label(self.detail_info_frame, text=" | Serves:", font=("Helvetica", 14), fg="#2c3e50", bg="#fff3e0").pack(side="left")
        self.detail_serves = tk.Label(self.detail_info_frame, font=("Helvetica", 14), fg="#2c3e50", bg="#fff3e0")
        self.detail_serves.pack(side="left", padx=5)

        # Ingredients Section
        tk.Label(self.scrollable_frame, text="Ingredients:", font=("Helvetica", 16, "bold"), fg="#2c3e50", bg="#fff3e0").pack(pady=5)
        self.ingredients_text = scrolledtext.ScrolledText(self.scrollable_frame, font=("Helvetica", 14), fg="#2c3e50", bg="#ffffff", wrap=tk.WORD, height=5, width=80)
        self.ingredients_text.pack(pady=5)

        # Steps Section
        tk.Label(self.scrollable_frame, text="Steps:", font=("Helvetica", 16, "bold"), fg="#2c3e50", bg="#fff3e0").pack(pady=5)
        self.steps_text = scrolledtext.ScrolledText(self.scrollable_frame, font=("Helvetica", 14), fg="#2c3e50", bg="#ffffff", wrap=tk.WORD, height=8, width=80)
        self.steps_text.pack(pady=5)

        # Feedback Input
        tk.Label(self.scrollable_frame, text="Your Feedback:", font=("Helvetica", 16, "bold"), fg="#2c3e50", bg="#fff3e0").pack(pady=10)
        self.feedback_text = tk.Text(self.scrollable_frame, height=4, width=60, font=("Helvetica", 12), bg="#ffffff", borderwidth=1, relief="flat")
        self.feedback_text.pack(pady=10)

        tk.Button(self.scrollable_frame, text="Submit Feedback", font=("Helvetica", 12), bg="#2ecc71", fg="white", relief="flat", command=self.submit_feedback, padx=20, pady=10).pack(pady=10)

        # Feedback List
        tk.Label(self.scrollable_frame, text="Feedbacks:", font=("Helvetica", 16, "bold"), fg="#2c3e50", bg="#fff3e0").pack(pady=10)
        self.feedback_list = scrolledtext.ScrolledText(self.scrollable_frame, height=8, width=60, font=("Helvetica", 12), bg="#ffffff", relief="flat", borderwidth=1, wrap=tk.WORD)
        self.feedback_list.pack(pady=10)

        # Navigation Buttons
        button_frame = tk.Frame(self.scrollable_frame, bg="#fff3e0")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Back to Category", font=("Helvetica", 14), bg="#ecf0f1", fg="#2c3e50", relief="flat", command=self.controller.show_recipes, padx=20, pady=10).pack(side="left", padx=10)
        tk.Button(button_frame, text="Back to Home", font=("Helvetica", 14), bg="#ecf0f1", fg="#2c3e50", relief="flat", command=self.controller.show_welcome, padx=20, pady=10).pack(side="left", padx=10)

    def update_details(self, recipe):
        """Update the details of the selected recipe."""
        self.detail_name.config(text=recipe["name"])

        # Update Image
        image = self.controller.get_random_image()
        if image:
            self.detail_image.image = image
            self.detail_image.config(image=image)

        # Update Recipe Details
        self.detail_time.config(text=recipe["time"])
        self.detail_serves.config(text=recipe["serves"])

        # Update Ingredients & Steps
        self.ingredients_text.delete(1.0, tk.END)
        self.ingredients_text.insert(tk.END, recipe["ingredients"])

        self.steps_text.delete(1.0, tk.END)
        self.steps_text.insert(tk.END, recipe["steps"])

        # Clear old feedback
        self.feedback_text.delete(1.0, tk.END)
        self.feedback_list.delete(1.0, tk.END)

        # Load new feedbacks
        feedbacks = self.controller.get_feedbacks(recipe["name"])
        for fb in feedbacks:
            self.feedback_list.insert(tk.END, f"- {fb['feedback']}\n")

    def submit_feedback(self):
        """Handles submitting feedback."""
        feedback = self.feedback_text.get(1.0, tk.END).strip()
        recipe_name = self.detail_name.cget("text")

        if not feedback:
            messagebox.showwarning("Error", "Please enter your feedback!")
            return

        self.controller.save_feedback(recipe_name, feedback)
        messagebox.showinfo("Success", "Feedback submitted!")

        # Clear input and refresh details
        self.feedback_text.delete(1.0, tk.END)
        if hasattr(self.controller, 'current_recipe_id'):
            self.update_details(self.controller.get_recipe_by_id(self.controller.current_recipe_id))
