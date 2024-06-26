# Personal Daily Reminder

# Prompt for a Single Tak:
task_description = input("Enter your task: ")

task_var = task_description

task_priority = input("Priority (high, medium, low): ")

priority_var = task_priority

time_bound_var = input("Is it time-bound (yes/no): ")


# Process the Task Based on Priority and Time Sensitivity

match priority_var:
  case "high":
    if time_bound_var == "yes":
      print(f"Reminder: '{task_var}' is a high priority task that requires immediate attention today!")
    else:
      print(f"Reminder: '{task_var}' is a high priority task that does not require immediate attention!")
  case "medium":
    if time_bound_var == "yes":
      print(f'{task_var} is a medium task that requires attention before the day ends.')
    else:
      print(f'{task_var} is a medium task that must be completed before the week ends.')
  case "low":
    if time_bound_var == "yes":
      print(f"Note: '{task_var}' is a low priority task but needs attention as soon as time is available .")
    else:
      print(f"Note: '{task_var}' is a low priority task. Consider completing it when you have free time.")