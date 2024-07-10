# Robust Division Calculator with Command Line Arguments

def safe_divide(numerator, denominator):
  try:
    return float(numerator) / float(denominator)
  except ZeroDivisionError:
    return print(f"Error: Cannot divide by zero.")
  except ValueError:
    return print(f"Error: Please enter numeric values only.")