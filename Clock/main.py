import tkinter as tk
from clock import Clock  # Import the Clock class
import time

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Change Clock Time")

        # Create canvas for clock
        self.canvas = tk.Canvas(root, width=250, height=250)
        self.canvas.grid(row=0, column=0, columnspan=3)

        # Create Clock object
        self.clock = Clock(self.canvas)

        # Time Variables
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        # Track scheduled update event
        self.timer_event = None

        # Label for showing time
        self.time_label = tk.Label(root, text="00:00:00", font=("Arial", 14))
        self.time_label.grid(row=1, column=0, columnspan=3, pady=5)

        # Controls
        self.start_button = tk.Button(root, text="Set Time", command=self.start_clock)
        self.start_button.grid(row=2, column=0)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_clock)
        self.stop_button.grid(row=2, column=2)

        # Initialize Clock
        self.update_clock()

    def update_clock(self):
        """Update the clock hands and increase time every second if running."""
        if self.running:
            self.seconds += 1
            if self.seconds >= 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes >= 60:
                self.minutes = 0
                self.hours += 1
            if self.hours >= 12:
                self.hours = 0  # 12-hour format

        # Update clock hands
        self.clock.draw_clock(self.hours, self.minutes, self.seconds)

        # Update time label
        time_str = f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
        self.time_label.config(text=time_str)

        # Schedule next update and store the event
        if self.running:
            self.timer_event = self.root.after(1000, self.update_clock)

    def start_clock(self):
        """Start or resume the clock without duplication."""
        if not self.running:
            self.running = True
            if self.timer_event:
                self.root.after_cancel(self.timer_event)  # Cancel any previous scheduled update
            self.update_clock()  # Start updating

    def stop_clock(self):
        """Stop the clock and cancel the scheduled event to prevent duplicate timers."""
        self.running = False
        if self.timer_event:
            self.root.after_cancel(self.timer_event)
            self.timer_event = None  # Reset timer event tracking


# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()
