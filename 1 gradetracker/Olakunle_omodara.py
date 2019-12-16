input_test = input("enter somethings eaten in last 24 hrs: ")

# 2/3[ ] print True if "dairy" is in the input or False if not
print("dairy" in input_test.lower())
print("It is", "dairy" in input_test.lower(), 'that "' + input_test + '" contains "dairy"')

# 4[ ] Check if "nuts" are in the input
print("It is", "nuts" in input_test.lower(), 'that "' + input_test + '" contains "nuts"')

# 4+[ ] Challenge: Check if "seafood" is in the input
print("It is", "seafood" in input_test.lower(), 'that "' + input_test + '" contains "seafood"')

# 4+[ ] Challenge: Check if "chocolate" is in the input
print("It is", "chocolate" in input_test.lower(), 'that "' + input_test + '" contains "chocolate"')