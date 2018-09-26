calories = 116
fat = 7.2
carbs = 11
sugar = 10
chocolatebars = input("how many chocolate bars did you eat?")

calories = str(calories * int(chocolatebars))
fat = str(fat * int(chocolatebars))
carbs = str(11 * int(chocolatebars))
sugar = str(10 * int(chocolatebars))

print("You've eaten " + str(chocolatebars) + " chocolate bars. This contained " + str(calories) + " calories, " + str(fat) + " fat, " + str(carbs) + " carbs and " + str(sugar) + " sugar.")