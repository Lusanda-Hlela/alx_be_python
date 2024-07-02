# Arithmetic Operations Function

def perform_operation(num1, num2, operation):
  # num1 = float(num1)
  # num2 = float(num2)
  # operation = str(input("Enter the operation to perform (add, subtract, multiply, divide): ")).lower()
  
  match operation:
    case "add":
      return num1 + num2
    case "subtract":
      return num1 - num2
    case "multiply":
      return num1 * num2
    case "divide":
      if num2 != 0:
        return num1 / num2
      else:
        return "Cannot divide by zero."
