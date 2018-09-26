print("*** LOVE TEST ***")
name1 = input("What is your name? ")
name2 = input("And the name of your lover? ")

name1 = name1.strip().lower()
name2 = name2.strip().lower()

print("Now checking " + name1 + " versus " + name2)

if name1 == name2:
    print("You have the same names, scary!")
elif name1 < name2:
    print("Your name is lesser, this will not be a good match")
elif name1 > name2:
    print("Your name is larger, this will be an excellent match")