import tkinter as tk
from datetime import datetime, timedelta

# Constants
YEAR_IN_SECONDS = 31536000  # Number of seconds in a year (365 days)
UPDATE_INTERVAL = 1000  # Update interval in milliseconds (1 second)
BLOOMINGTON_TIMEZONE_OFFSET = -4  # Eastern Daylight Time (UTC-4)

# Function to calculate age in seconds
def calculate_age_in_seconds(birthdate, birthtime):
    birth_month, birth_day, birth_year = int(birthdate[:2]), int(birthdate[2:4]), int(birthdate[4:])
    birth_hour, birth_minute, birth_second = int(birthtime[:2]), int(birthtime[2:4]), int(birthtime[4:])
    birth_datetime = datetime(birth_year, birth_month, birth_day, birth_hour, birth_minute, birth_second)
    
    current_datetime = datetime.now() - timedelta(hours=BLOOMINGTON_TIMEZONE_OFFSET)
    age_timedelta = current_datetime - birth_datetime
    age_in_seconds = age_timedelta.total_seconds()
    
    return age_in_seconds

# Function to update age and countdown for different time periods
def update_age_countdown():
    birthdate = birthdate_entry.get()
    birthtime = birthtime_entry.get()
    
    if birthdate and birthtime:
        birth_month, birth_day, age_in_seconds = int(birthdate[:2]), int(birthdate[2:4]), calculate_age_in_seconds(birthdate, birthtime)
        percentage = (age_in_seconds / YEAR_IN_SECONDS) * 360
        current_time = datetime.now()
        next_birthday = datetime(current_time.year, birth_month, birth_day)
        
        if current_time > next_birthday:
            next_birthday = next_birthday.replace(year=current_time.year + 1)
            years_passed = current_time.year - int(birthdate[4:])
        else:
            years_passed = current_time.year - int(birthdate[4:])

        remaining_time = next_birthday - current_time
        months, remaining_days = divmod(remaining_time.days, 30)
        weeks, remaining_days = divmod(remaining_days, 7)
        days = remaining_days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        countdown_text.set(f"{years_passed}Y {months}M {weeks}W {days}D {hours}H {minutes}M {seconds}S")
        canvas.delete("year_circle")
        canvas.create_arc(10, 10, 190, 190, start=90 - percentage, extent=percentage, outline="purple", width=2, tags="year_circle")
        canvas.create_text(100, 170, text="This Year", font=("Helvetica", 12), fill="white")

        # Update other time period graphs with consistent design
        update_time_period_graph("This Month", months, 12, "blue", 1)
        update_time_period_graph("This Week", weeks, 4.33, "lightblue", 2)
        update_time_period_graph("This Day", days, 30, "deepskyblue", 3)
        update_time_period_graph("This Hour", hours, 24, "dodgerblue", 4)
        update_time_period_graph("This Minute", minutes, 60, "royalblue", 5)
        
        # Update the top clock to count up
        top_clock_seconds.set(int(top_clock_seconds.get()) + 1)
        if int(top_clock_seconds.get()) >= 60:
            top_clock_seconds.set(0)
            top_clock_minutes.set(int(top_clock_minutes.get()) + 1)
            if int(top_clock_minutes.get()) >= 60:
                top_clock_minutes.set(0)
                top_clock_hours.set(int(top_clock_hours.get()) + 1)
    else:
        countdown_text.set("")  # Clear the text when birthdate is empty

    root.after(UPDATE_INTERVAL, update_age_countdown)

# Function to update time period graphs
def update_time_period_graph(period_name, current_value, max_value, color, row):
    percentage = (current_value / max_value) * 360
    canvas.delete(f"{period_name}_circle")
    canvas.create_arc(250, 10 + (row * 60), 430, 190 + (row * 60), start=90 - percentage, extent=percentage, outline=color, width=2, tags=f"{period_name}_circle")
    canvas.create_text(340, 30 + (len(period_name) * 10) + (row * 60), text=period_name, font=("Helvetica", 12), fill="white")

# Function to close the window and exit the program
def close_window():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Age Progression")
root.geometry("900x700")
root.configure(bg="black")

# Create a canvas for the circular graphs
canvas = tk.Canvas(root, width=420, height=400, bg="black")
canvas.grid(row=5, column=0, columnspan=6)

# Create a label to display the countdown
countdown_text = tk.StringVar()
countdown_label = tk.Label(root, textvariable=countdown_text, font=("Helvetica", 16), fg="white", bg="black")
countdown_label.grid(row=4, column=0, columnspan=6, pady=10)

# Create an entry to input birthdate and birthtime
birthdate_label = tk.Label(root, text="Enter your birthdate (MMDDYYYY):", font=("Helvetica", 12), fg="white", bg="black")
birthdate_label.grid(row=0, column=0, padx=20, pady=5, sticky="e")
birthdate_entry = tk.Entry(root, font=("Helvetica", 12))
birthdate_entry.grid(row=0, column=1, padx=20, pady=5, sticky="w")

birthtime_label = tk.Label(root, text="Enter your birthtime (HHMMSS):", font=("Helvetica", 12), fg="white", bg="black")
birthtime_label.grid(row=1, column=0, padx=20, pady=5, sticky="e")
birthtime_entry = tk.Entry(root, font=("Helvetica", 12))
birthtime_entry.grid(row=1, column=1, padx=20, pady=5, sticky="w")

# Create a button to update age and countdown
update_button = tk.Button(root, text="Update", command=update_age_countdown, font=("Helvetica", 12))
update_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create a button to close the window
close_button = tk.Button(root, text="Close", command=close_window, font=("Helvetica", 12))
close_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create variables to display the top clock
top_clock_hours = tk.StringVar()
top_clock_minutes = tk.StringVar()
top_clock_seconds = tk.StringVar()
top_clock_hours.set("00")
top_clock_minutes.set("00")
top_clock_seconds.set("00")

# Create labels for the top clock
top_clock_label = tk.Label(root, textvariable=top_clock_hours, font=("Helvetica", 20), fg="white", bg="black")
top_clock_label.grid(row=4, column=0, columnspan=2, pady=10)
top_clock_colon1 = tk.Label(root, text=":", font=("Helvetica", 20), fg="white", bg="black")
top_clock_colon1.grid(row=4, column=2)
top_clock_minutes_label = tk.Label(root, textvariable=top_clock_minutes, font=("Helvetica", 20), fg="white", bg="black")
top_clock_minutes_label.grid(row=4, column=3)
top_clock_colon2 = tk.Label(root, text=":", font=("Helvetica", 20), fg="white", bg="black")
top_clock_colon2.grid(row=4, column=4)
top_clock_seconds_label = tk.Label(root, textvariable=top_clock_seconds, font=("Helvetica", 20), fg="white", bg="black")
top_clock_seconds_label.grid(row=4, column=5)

# Initialize the circular graphs
for row, period_name, color in zip(range(5, 11), ["This Year", "This Month", "This Week", "This Day", "This Hour", "This Minute"], ["purple", "blue", "lightblue", "deepskyblue", "dodgerblue", "royalblue"]):
    update_time_period_graph(period_name, 0, 1, color, row)

# Run the main loop
root.after(UPDATE_INTERVAL, update_age_countdown)
root.mainloop()
