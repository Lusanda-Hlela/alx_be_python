# Personal Daily Reminder

# Prompt for a Single Task:
task_reminder = input("Enter your task: ")

# Process the Task Based on Priority and Time Sensitivity:
priority = input("Priority (high/medium/low): ")

urgency = input("Is it time-bound? (yes/no): ")


# Provide a Customized Reminder:
match priority:
  case "high":
    reminder = f"Reminder: '{task_reminder}' is a high priority task"
    if urgency == "yes":
      reminder += " that requires immediate attention today!"
    else:
      reminder += " that can wait until tomorrow!"
  case "medium":
    reminder = f"Reminder: '{task_reminder}' is a medium priority task"
    if urgency == "yes":
      reminder += " that requires some attention today."
    else:
      reminder += " that can wait until tomorrow!"
  case "low":
    reminder = f"Reminder: '{task_reminder}' is a low priority task"
    if urgency == "yes":
      reminder += " that must be completed today."
    else:
      reminder = f"Note: '{task_reminder}' is a low priority task. Consider completing it when you have free time."

# Display the Reminder:
print(reminder)