import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from PIL import Image, ImageTk

class HolidayReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Reminder By Jason Hoyle")
        self.root.geometry("500x400")
        
        # Load the campervan image and set as background
        self.background_image = Image.open("campervan.jpg")  # Replace with the path to your campervan image
        self.background_image = self.background_image.resize((500, 400), Image.Resampling.LANCZOS)  # Fixed line
        self.bg_image = ImageTk.PhotoImage(self.background_image)

        self.canvas = tk.Canvas(self.root, width=500, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Labels and Inputs
        self.canvas.create_text(250, 50, text="Enter Holiday Date (DD/MM/YYYY):", font=("Helvetica", 14), fill="white")
        self.date_entry = ttk.Entry(self.root, font=("Helvetica", 12), width=20)
        self.date_entry_window = self.canvas.create_window(250, 100, window=self.date_entry)

        # Button to start countdown
        self.start_button = ttk.Button(self.root, text="Start Countdown Carol", command=self.start_countdown)
        self.start_button_window = self.canvas.create_window(250, 150, window=self.start_button)

        # Countdown label
        self.countdown_label = ttk.Label(self.root, text="", font=("Helvetica", 14, "bold"), background="white")
        self.countdown_label_window = self.canvas.create_window(250, 250, window=self.countdown_label)

    def start_countdown(self):
        # Get the date input
        date_str = self.date_entry.get()
        try:
            holiday_date = datetime.strptime(date_str, "%d/%m/%Y")
            today = datetime.now()

            # Calculate the difference between the holiday date and today
            if holiday_date > today:
                delta = holiday_date - today
                days_left = delta.days
                hours_left = delta.seconds // 3600
                minutes_left = (delta.seconds % 3600) // 60
                seconds_left = delta.seconds % 60

                self.countdown_label.config(text=f"Time left: {days_left} Days, {hours_left} Hours, "
                                                 f"{minutes_left} Minutes, {seconds_left} Seconds")

                # Update countdown every second
                self.root.after(1000, self.start_countdown)
            else:
                self.countdown_label.config(text="The holiday date has passed!")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter the date in DD/MM/YYYY format.")

# Create the main window
root = tk.Tk()

# Create an instance of the HolidayReminderApp class
app = HolidayReminderApp(root)

# Start the Tkinter event loop
root.mainloop()