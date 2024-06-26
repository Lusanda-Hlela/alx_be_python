# Weather Recommendation Program

# Ask the user about the current weather conditions and provide clothing recommendations based on the user input

current_weather_conditions = input("What's the weather like today? (sunny/rainy/cold): ")

if current_weather_conditions == "sunny":
  print("Wear a t-shirt and sunglasses.")
elif current_weather_conditions == "rainy":
  print("Don't forget you umbrella and a raincoat.")
elif current_weather_conditions == "cold":
  print("Make sure to wear a warm coat and a scarf.")
else:
  print("Sorry, I don't have recommendations for this weather.")