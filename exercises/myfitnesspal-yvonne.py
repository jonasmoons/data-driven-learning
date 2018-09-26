# Brinky Nutritional Value #
kcal = 115.2
carbs = 16.6
fat = 4.8
eggwhite = 1.3

# Ask user for amount of cookies #
amount = input("How many Brinkies did you eat?")

# Calculate #
calories = int(amount) * kcal
carbohydrates = int(amount) * carbs
fats = int(amount) * fat
eggwhites = int(amount) * eggwhite


# Print to the user #
print("The amount of calories in " + str(amount) + " Brinkies is " + str(calories) + " kcal.")
print("Also, there's " + str(carbohydrates) + " carbs, " + str(fats) + " grams of fat and " + str(eggwhites) + " grams of egg white.")