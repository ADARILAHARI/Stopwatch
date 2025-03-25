import tkinter as tk
from threading import Thread
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch Timer")
        self.running = False
        self.counter = 0
        self.reminder_time = 0
        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack()
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack()
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack()
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack()
        self.reminder_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.reminder_label.pack()
        
        # Preset time slots (in seconds)
        self.time_options = [10, 30, 60, 120, 300]
        self.time_var = tk.IntVar(value=self.time_options[0])
        self.create_time_buttons()

    def create_time_buttons(self):
        for option in self.time_options:
            time_button = tk.Radiobutton(self.root, text=f"{option} seconds", variable=self.time_var, value=option)
            time_button.pack()

    def update_label(self):
        while self.running:
            time.sleep(1)
            self.counter += 1
            minutes, seconds = divmod(self.counter, 60)
            hours, minutes = divmod(minutes, 60)
            time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.label.config(text=time_str)
            remaining_time = self.reminder_time - self.counter
            if remaining_time > 0:
                self.reminder_label.config(text=f"Time left: {remaining_time} seconds")
            else:
                self.reminder_label.config(text="Time's up!")
            self.root.update()

    def start(self):
        if not self.running:
            self.running = True
            self.reminder_time = self.time_var.get()
            self.thread = Thread(target=self.update_label)
            self.thread.start()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.counter = 0
        self.label.config(text="00:00:00")
        self.reminder_label.config(text="")

# Create the main window
root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()



'''import tkinter as tk
from threading import Thread
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch Timer")
        self.running = False
        self.counter = 0
        self.reminder_time = 0
        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack()
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack()
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack()
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack()
        self.reminder_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.reminder_label.pack()
        self.reminder_entry = tk.Entry(root)
        self.reminder_entry.pack()
        self.reminder_button = tk.Button(root, text="Set Reminder", command=self.set_reminder)
        self.reminder_button.pack()

    def update_label(self):
        while self.running:
            time.sleep(1)
            self.counter += 1
            minutes, seconds = divmod(self.counter, 60)
            hours, minutes = divmod(minutes, 60)
            time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.label.config(text=time_str)
            if self.counter == self.reminder_time:
                self.reminder_label.config(text=self.reminder_entry.get())
            self.root.update()

    def start(self):
        if not self.running:
            self.running = True
            self.thread = Thread(target=self.update_label)
            self.thread.start()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.counter = 0
        self.label.config(text="00:00:00")
        self.reminder_label.config(text="")

    def set_reminder(self):
        reminder = self.reminder_entry.get()
        self.reminder_time = self.counter + int(reminder)

# Create the main window
root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()


'''
