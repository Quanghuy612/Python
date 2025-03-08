import math
import tkinter as tk

class Clock:
    def __init__(self, canvas):
        self.canvas = canvas
        self.center_x = 125
        self.center_y = 125
        self.radius = 100

    def draw_clock(self, hours, minutes, seconds):
        self.canvas.delete("all")  # Clear previous drawings

        # Draw clock face
        self.canvas.create_oval(
            self.center_x - self.radius, self.center_y - self.radius,
            self.center_x + self.radius, self.center_y + self.radius,
            outline="black", width=2
        )

        # Convert time to angles
        second_angle = (seconds * 2 * math.pi / 60) - (math.pi / 2)
        minute_angle = (minutes * 2 * math.pi / 60) - (math.pi / 2)
        hour_angle = ((hours % 12 + minutes / 60) * 2 * math.pi / 12) - (math.pi / 2)

        # Draw hands
        self.draw_hand(second_angle, self.radius * 0.9, "red", 2)
        self.draw_hand(minute_angle, self.radius * 0.7, "black", 3)
        self.draw_hand(hour_angle, self.radius * 0.5, "black", 4)

    def draw_hand(self, angle, length, color, width):
        x = self.center_x + length * math.cos(angle)
        y = self.center_y + length * math.sin(angle)
        self.canvas.create_line(self.center_x, self.center_y, x, y, fill=color, width=width)
