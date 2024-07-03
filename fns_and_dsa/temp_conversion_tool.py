# Temperature Conversion Tool

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Prompt the user for a numeric temperature value
def get_temperature():
  while True:
    try:
      temperature = int(input("Enter the temperature to convert: "))
      return temperature
    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

def convert_to_celsius(fahrenheit):
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Correct temperature data type
temperature = get_temperature()

# Prompt the user for the desired temperature units
units = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if units == "C":
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
elif units == "F":
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
else:
    print("Invalid temperature units. Please enter °C for Celsius and °F for Fahrenheit.")
