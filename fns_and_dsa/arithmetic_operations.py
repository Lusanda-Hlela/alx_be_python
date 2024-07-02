# Arithmetic Operations Function

def perform_operation(num1, num2, operation):
  match operation:
    case "add":
      return num1 + num2
    case "subtract":
      return num1 - num2
    case "multiply":
      return num1 * num2
    case "divide":
      if num2 == 0:
        return "Cannot divide by zero."
      elif (num1 < 0 ) or (num2 < 0):
        return "Only positive numbers are allowed."
      else:
        return num1 / num2