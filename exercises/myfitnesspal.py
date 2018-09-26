# Nutritional values for one Oreo cookie
# Source: https://www.fitbit.com/foods/Oreo+Cookie/16421
calories = 50
fat = 2.3
carbs = 8.3
sugar = 4.7

nr_of_cookies = input("How many Oreo cookies did you eat? ")
print("You had " + nr_of_cookies + " cookies")

# Convert to float, because the user might have had part of a cookie
nr_of_cookies = float(nr_of_cookies)

# And calculate the user values
user_calories = calories * nr_of_cookies
user_fat = fat * nr_of_cookies
user_carbs = carbs * nr_of_cookies
user_sugar = sugar * nr_of_cookies

print("Calories: " + str(user_calories))
print("Fat: " + str(user_fat) + " grams")
print("Carbs: " + str(user_carbs) + " grams")
print("Sugar: " + str(user_sugar) + " grams")