import os
import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from win10toast import ToastNotifier


class PomodoroTimer:
    def __init__(self, root, countdown_time):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("400x400")
        self.root.configure(bg="#FFCCCC")
        self.root.attributes('-topmost', True)

        self.notifier = ToastNotifier()

        # 默认时间设置
        self.work_time = 25 * 60
        self.short_break = 5 * 60
        self.long_break = 15 * 60
        self.initial_time = countdown_time
        self.time_left = countdown_time
        self.running = False

        # 日志文件路径
        self.log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pomodoro_log.csv')
        self.task_name = "Unnamed Task"

        # UI 元素
        self.label_time = tk.Label(
            root, text=self.format_time(self.time_left), font=("Impact", 36), bg="#FFCCCC", fg="#D24D57"
        )
        self.label_time.pack(pady=10)

        # 按钮区域
        self.button_frame = tk.Frame(root, bg="#FFCCCC")
        self.button_frame.pack(pady=10)
        self.toggle_button = ttk.Button(self.button_frame, text="START!", command=self.toggle_timer)
        self.toggle_button.grid(row=0, column=0, padx=5)
        self.settings_button = ttk.Button(self.button_frame, text="Settings", command=self.open_settings)
        self.settings_button.grid(row=0, column=1, padx=5)
        self.stats_button = ttk.Button(self.button_frame, text="Stats", command=self.show_stats)
        self.stats_button.grid(row=0, column=2, padx=5)

        # 任务板
        self.task_label = tk.Label(root, text="Task Board", font=("Arial", 14), bg="#FFCCCC", fg="black")
        self.task_label.pack()
        self.task_frame = tk.Frame(root, bg="#FFCCCC")
        self.task_frame.pack(fill=tk.BOTH, expand=True)
        self.task_tree = ttk.Treeview(self.task_frame, columns=("Task", "Status"), show="headings", height=5)
        self.task_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.task_tree.heading("Task", text="Task")
        self.task_tree.heading("Status", text="Status")
        self.task_tree.column("Task", width=200)
        self.task_tree.column("Status", width=100)

        self.task_scroll = ttk.Scrollbar(self.task_frame, orient="vertical", command=self.task_tree.yview)
        self.task_tree.configure(yscrollcommand=self.task_scroll.set)
        self.task_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # 任务板按钮
        self.task_buttons_frame = tk.Frame(root, bg="#FFCCCC")
        self.task_buttons_frame.pack()
        self.add_task_button = ttk.Button(self.task_buttons_frame, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=0, padx=5)
        self.complete_task_button = ttk.Button(self.task_buttons_frame, text="Complete Task", command=self.complete_task)
        self.complete_task_button.grid(row=0, column=1, padx=5)
        self.delete_task_button = ttk.Button(self.task_buttons_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=0, column=2, padx=5)

        self.update_clock()

    def format_time(self, seconds):
        """Format time in MM:SS."""
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02}:{seconds:02}"

    def toggle_timer(self):
        """Start or pause the timer."""
        if self.running:
            self.running = False
            self.toggle_button.config(text="RESUME!")
        else:
            self.running = True
            self.toggle_button.config(text="PAUSE!")

    def update_clock(self):
        """Update the countdown clock every second."""
        if self.running:
            if self.time_left > 0:
                self.time_left -= 1
                self.animate_time()
                self.label_time.config(text=self.format_time(self.time_left))
            else:
                self.running = False
                self.log_time()
                self.notify_user("Time's up!", "Take a short break or start a new task.")
                messagebox.showinfo("Pomodoro Timer", "Time's up!")
                return
        self.root.after(1000, self.update_clock)

    def log_time(self):
        """Log completed pomodoro session to CSV file."""
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        duration_minutes = self.initial_time // 60
        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, duration_minutes, self.task_name])

    def notify_user(self, title, message):
        """Show a system notification."""
        self.notifier.show_toast(title, message, duration=5, threaded=True)

    def open_settings(self):
        """Open settings dialog to modify timer values."""
        self.work_time = int(simpledialog.askstring("Work Time", "Enter work time (minutes):")) * 60
        self.short_break = int(simpledialog.askstring("Short Break", "Enter short break time (minutes):")) * 60
        self.long_break = int(simpledialog.askstring("Long Break", "Enter long break time (minutes):")) * 60
        self.task_name = simpledialog.askstring("Task Name", "Enter task name:")

        # 更新倒计时时间
        self.time_left = self.work_time  # 重新设置倒计时的初始时间
        self.label_time.config(text=self.format_time(self.time_left))  # 更新UI显示的时间

    '''def open_settings(self):
        """Open settings dialog to modify timer values."""
        self.work_time = int(simpledialog.askstring("Work Time", "Enter work time (minutes):")) * 60
        self.short_break = int(simpledialog.askstring("Short Break", "Enter short break time (minutes):")) * 60
        self.long_break = int(simpledialog.askstring("Long Break", "Enter long break time (minutes):")) * 60
        self.task_name = simpledialog.askstring("Task Name", "Enter task name:")'''

    def show_stats(self):
        """Show the stats of completed pomodoro sessions."""
        total_sessions = 0
        total_minutes = 0
        if os.path.exists(self.log_file):
            with open(self.log_file, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    total_sessions += 1
                    total_minutes += int(row[1])

        stats_message = f"Total Sessions: {total_sessions}\nTotal Time: {total_minutes} minutes"
        messagebox.showinfo("Pomodoro Stats", stats_message)

    def add_task(self):
        """Add a new task to the task list."""
        task = simpledialog.askstring("Add Task", "Enter task description:")
        if task:
            self.task_tree.insert("", tk.END, values=(task, "Pending"))

    def complete_task(self):
        """Mark selected task as completed."""
        selected_item = self.task_tree.selection()
        if selected_item:
            self.task_tree.item(
                selected_item, values=(self.task_tree.item(selected_item, "values")[0], "Completed")
            )

    def delete_task(self):
        """Delete selected task from the list."""
        selected_item = self.task_tree.selection()
        if selected_item:
            self.task_tree.delete(selected_item)

    def animate_time(self):
        """Animate the timer label to change font size."""
        self.label_time.config(font=("Impact", 40))
        self.root.after(200, lambda: self.label_time.config(font=("Impact", 36)))


def main():
    """Main function to run the pomodoro timer."""
    root = tk.Tk()
    countdown_time = 25 * 60
    timer = PomodoroTimer(root, countdown_time)
    root.mainloop()


if __name__ == "__main__":
    main()
