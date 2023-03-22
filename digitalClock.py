import tkinter as tk
from time import strftime

def update_time():
    time_str = strftime('%H:%M:%S %p')
    clock_label.config(text=time_str)
    clock_label.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title('Digital Clock')

# Create a label for the clock display
clock_label = tk.Label(root, font=('Helvetica', 60))
clock_label.pack()

# Update the time every second
update_time()

# Start the event loop
root.mainloop()