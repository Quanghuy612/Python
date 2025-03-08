import tkinter as tk
import random

class Sudoku:
    MAX_CELL = 9  # 9x9 Sudoku Grid

    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Validator")

        # Create main frame
        self.frame = tk.Frame(root, padx=10, pady=10)
        self.frame.pack()

        # Set up grid layout
        self.entries = [[None] * self.MAX_CELL for _ in range(self.MAX_CELL)]

        for row in range(self.MAX_CELL):
            for col in range(self.MAX_CELL):
                entry = tk.Entry(self.frame, width=2, font=("Arial", 18), justify="center", 
                                 validate="key", validatecommand=(self.root.register(self.validate_input), "%P"))
                entry.grid(row=row, column=col, ipadx=5, ipady=5, padx=2, pady=2)
                self.entries[row][col] = entry

        # Buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.validate_button = tk.Button(self.button_frame, text="Validate", font=("Arial", 12), command=self.validate_sudoku)
        self.validate_button.grid(row=0, column=0, padx=5)

        self.generate_button = tk.Button(self.button_frame, text="Generate Example", font=("Arial", 12), command=self.generate_random_grid)
        self.generate_button.grid(row=0, column=1, padx=5)

        # Label for validation result
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=5)

    def validate_input(self, P):
        """Allows only numbers 1-9"""
        return P == "" or (P.isdigit() and 1 <= int(P) <= 9)

    def generate_random_grid(self):
        """Fills the grid with completely random numbers (1-9)"""
        for row in range(self.MAX_CELL):
            for col in range(self.MAX_CELL):
                num = random.randint(1, 9)  # Completely random number (may not follow Sudoku rules)
                self.entries[row][col].delete(0, tk.END)
                self.entries[row][col].insert(0, str(num))

    def validate_sudoku(self):
        """Checks if each row and column contains unique numbers (1-9)"""
        grid = [[self.entries[row][col].get() for col in range(self.MAX_CELL)] for row in range(self.MAX_CELL)]

        for i in range(self.MAX_CELL):
            row_nums = set()
            col_nums = set()

            for j in range(self.MAX_CELL):
                row_val = grid[i][j]
                col_val = grid[j][i]

                if row_val:
                    if row_val in row_nums:
                        self.result_label.config(text="Invalid solution")
                        return
                    row_nums.add(row_val)

                if col_val:
                    if col_val in col_nums:
                        self.result_label.config(text="Invalid solution")
                        return
                    col_nums.add(col_val)

        self.result_label.config(text="Valid solution")
  

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = Sudoku(root)
    root.mainloop()
