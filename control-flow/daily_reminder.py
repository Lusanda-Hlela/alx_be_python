# Personal Daily Reminder

# Prompt the user for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder variable
reminder = f"Reminder: '{task}' is a {priority} priority task"

# Process the task based on priority and time sensitivity

match priority:
  case "high":
    if time_bound == "yes":
      reminder = reminder + " that requires immediate attention today!"
    else:
      reminder = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
  case "medium":
    if time_bound == "yes":
      reminder = reminder + " that you should try to complete today."
    else:
      reminder = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
  case "low":
    if time_bound == "yes":
      reminder = reminder + " that you should try to complete today."
    else:
      reminder = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."

print(reminder)