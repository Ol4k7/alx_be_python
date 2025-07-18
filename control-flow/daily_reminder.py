# daily_reminder.py

# Prompt the user to input task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using Match Case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Note: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an undefined priority level"

# Adjust the message based on time-bound status
if time_bound == "yes":
    message += " that requires immediate attention today!"
elif time_bound == "no":
    message += ". Consider completing it when you have free time."
else:
    message += ". (Time-bound status unclear.)"

# Output the final reminder
print("\n" + message)
