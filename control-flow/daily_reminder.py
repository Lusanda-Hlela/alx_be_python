# daily_reminder.py

# Prompt the user for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder variable
reminder = f"'{task}' is a {priority} priority task"

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". You should complete this task as soon as possible."
    case "medium":
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". You should complete this task when possible."
    case "low":
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

# Provide a Customized Reminder
if priority == "low" and time_bound != "yes":
  print(reminder)
else:
  print(f"Reminder: {reminder}")