# Personal Daily Reminder

# Prompt for a Single Task:
task_reminder = input("Enter your task: ")

# Process the Task Based on Priority and Time Sensitivity:
priority = input("Priority (high/medium/low): ").lower()

urgency = input("Is it time-bound? (yes/no): ").lower()


# Provide a Customized Reminder:
reminder = f"'{task_reminder}' is a {priority} priority task"

if urgency == "yes":
  time_bound = " that requires immediate attention today!"
else:
  time_bound = ""

match priority:
  case "high":
    reminder += time_bound if time_bound else " that you should complete as soon as possible."
    print(f"Reminder: {reminder}")
  case "medium":
    reminder += time_bound if time_bound else " that you should complete when possible."
    print(f"Reminder: {reminder}")
  case "low":
    reminder += time_bound if time_bound else " that you should completing when you have free time."
    print(f"Note: {reminder}")