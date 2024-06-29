# Personal Daily Reminder

# Prompt for a Single Task:
task_reminder = input("Enter your task: ")

# Process the Task Based on Priority and Time Sensitivity:
priority = input("Priority (high/medium/low): ")

urgency = input("Is it time-bound? (yes/no): ")


# Provide a Customized Reminder:

if urgency == "yes":
  match priority:
    case "high":
      print(f"Reminder: '{task_reminder}' is a high priority task that requires immediate attention today!")
    case "medium":
      print(f"Reminder: '{task_reminder}' is a medium priority task that requires immediate attention today!")
    case "low":
      print(f"Reminder: '{task_reminder}' is a low priority task that requires immediate attention today!")
else:
  print(f"Note: '{task_reminder}' is a low priority task. Consider completing it when you have free time.")