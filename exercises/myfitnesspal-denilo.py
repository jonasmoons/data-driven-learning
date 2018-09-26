#nutritional values
sugar = 4.7
fat = 2.3
carbs = 8.3
calories = 53.3

# multiplying by the amount
amount = input(“How many oreo’s did you eat?“)
total_sugar = float(amount) * sugar
total_fat = float(amount) * fat
total_carbs = float(amount) * carbs
total_calories = float(amount)* calories

#print statement
print(“You ate” +” “+  str(amount) + ” ” +  “oreo’s. This contains ” + str(total_sugar) +‘gr sugar, ’ + str(total_fat) + ‘gr fat, ’ + str(total_carbs) + ‘gr carbs and has a total of ’ + str(total_calories) + ‘calories.’)