# Personal Daily Reminder

# Prompt for a Single Task:
task_reminder = input("Enter your task: ")

# Process the Task Based on Priority and Time Sensitivity:
priority = input("Priority (high/medium/low): ")

urgency = input("Is it time-bound? (yes/no): ")


# Provide a Customized Reminder:

match priority:
  case "high":
    if urgency == "yes":
      print(f"Reminder: '{task_reminder}' is a high priority task that requires immediate attention today!")
  case "medium":
    if urgency == "yes":
      print(f"Reminder: '{task_reminder}' is a medium priority task that does not require immediate attention today. Please give attention the task once all high priority tasks have been completed")
  case "low":
    if urgency == "yes":
      print(f"Reminder: '{task_reminder}' is a low priority task that requires attention only when high and medium priority tasks that are time-bound have been completed")
    else:
      print(f"Note: '{task_reminder}' is a low priority task. Consider completing it when you have free time.")