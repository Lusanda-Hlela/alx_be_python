# Temperature Conversion Tool

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = int(input("Enter the temperature to convert: "))
units = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def convert_to_celsius(fahrenheit):
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if units == "C" and type(temperature) == int:
  print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
elif units == "F" and type(temperature) == int:
  print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
else:
  print("Invalid temperature. Please enter a numeric value")