# Pomodoro Timer - A Desktop Application for Time Management

## Overview

The **Pomodoro Timer** is a desktop application designed to implement the Pomodoro Technique, a time management method developed by Francesco Cirillo. This technique uses intervals of work and short breaks to improve productivity and focus. The application allows users to customize work and break durations, track their progress, and manage tasks efficiently.

## Features

- **Customizable Timer**: Users can set their work, short break, and long break durations.
- **Real-Time Countdown**: The timer updates every second, providing real-time feedback on the elapsed time.
- **Task Management**: The application includes a task board where users can add, mark, and delete tasks, with the ability to track the status of each task.
- **Pomodoro Session Logging**: Each completed Pomodoro session is logged with a timestamp and task name.
- **Statistics**: Users can view statistics on the number of completed sessions and total time spent working.
- **Notifications**: System notifications are displayed when the timer completes a session, reminding the user to take a break or start a new task.

## Requirements

The following Python libraries are required to run the application:

- `tkinter` – Standard library for building the GUI.
- `win10toast` – For system notifications (only supported on Windows).
- `csv` – For logging Pomodoro session data.
- `datetime` – For timestamping the Pomodoro sessions.
- `os` – For handling file paths.

The application is intended to run on Windows. However, it could be adapted to other operating systems with minor modifications, especially regarding system notifications.

## Installation

1. Clone or download the repository.

2. Ensure Python is installed (version 3.6 or higher recommended).

3. Install the required Python packages:

   ```bash
   pip install win10toast
   ```

4. Run the `pomodoro_timer.py` file:

   ```bash
   python pomodoro_timer.py
   ```

## Usage

Upon running the application, the following features are available:

1. **Main Interface**:
   - A timer display shows the remaining time in minutes and seconds.
   - Buttons allow users to start, pause, and configure the timer settings.
2. **Settings**:
   - Users can adjust the work duration, short break duration, and long break duration.
   - Users can also input a task name that will be logged with each Pomodoro session.
3. **Task Management**:
   - A task board is available to add, mark as completed, or delete tasks.
   - Tasks can be marked with the status “Pending” or “Completed.”
4. **Statistics**:
   - View the total number of Pomodoro sessions and the total time spent on all sessions.
   - These statistics are based on data stored in a CSV log file.
5. **Notifications**:
   - Upon completion of each Pomodoro session, a notification is triggered.
   - A message is also displayed via a dialog box, notifying the user that the session is complete.

## Example Workflow

1. **Configure Timer**:
   - Set your preferred work time, short break time, and long break time via the Settings menu.
2. **Start Working**:
   - Click "START!" to begin a Pomodoro session. The timer will count down the configured work time.
3. **Task Management**:
   - Add tasks to the task board, mark tasks as completed, and delete tasks as needed.
4. **Take Breaks**:
   - Once the work time is complete, the application will notify you and suggest taking a short break. After the break, you can start a new Pomodoro session.
5. **Track Progress**:
   - View statistics on completed sessions and total time worked through the "Stats" button.

## Code Structure

### Main Class: `PomodoroTimer`

The core of the application is encapsulated in the `PomodoroTimer` class, which handles the following responsibilities:

- **Initialization**: Set up the GUI and initialize variables such as work time, break time, and session status.
- **Timer Control**: The timer countdown is managed using the `update_clock` method, which runs every second to update the remaining time.
- **Task Management**: The task board is implemented using a `Treeview` widget, which allows users to manage tasks.
- **Session Logging**: Each Pomodoro session is logged to a CSV file using the `log_time` method, including the timestamp, session duration, and task name.
- **Settings**: The `open_settings` method allows users to customize the timer's duration and task name.
- **Statistics**: The `show_stats` method reads the CSV log file to provide statistics on completed sessions and total time worked.

### GUI Elements

- **Timer Display**: The remaining time is shown in a large label.
- **Control Buttons**: Buttons for starting, pausing, and configuring the timer.
- **Task Board**: A `Treeview` widget displays tasks and their statuses (Pending or Completed).
- **Statistics Display**: The number of completed Pomodoro sessions and total time worked is displayed in a pop-up window.

## Logging and Statistics

The application logs each completed Pomodoro session to a CSV file, which is stored in the same directory as the script. The log file is structured as follows:

```
timestamp, duration_minutes, task_name
```

For example:

```
2024-11-23 10:15:00, 25, "Write Research Paper"
```

This log can be used to track work habits and productivity over time.

## Contribution

Contributions are welcome. If you have suggestions or improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the Apache-2.0 License.

## Contact

For any questions or suggestions, please contact the project maintainers.

