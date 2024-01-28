# I'll first refactor your existing code for clarity and then extend it with the features you requested: Fahrenheit to Celsius conversion and a personalized story about the user's pet.

# Arithmetic operations
print(10 / 3)   # Division
print(10 // 3)  # Floor division
print(10 % 3)   # Modulus
print(10 ** 3)  # Exponent
print(10 + 3)   # Addition

# Incrementing x
x = 10
x = x + 3
x += 3

# Temperature check
temperature = 35
if temperature >= 30:
    print("It's hot")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
    print("Wear warm clothes")

# Weight conversion
weight = int(input("What is your Weight? "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.453592
    print("Your Weight in Lbs is " + str(converted))
elif unit.upper() == "L":
    converted = weight * 0.453592
    print("Your Weight in Kg is " + str(converted))
else:
    print("Invalid input")

# Fahrenheit to Celsius conversion
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5.0/9.0
print(f'{fahrenheit} Fahrenheit is {celsius} Celsius')

# Pet information
pet_name = input("What's your pet's name? ")
pet_type = input("What type of pet is it? (e.g., dog, cat, bird) ")
pet_age = input("How old is your pet? ")

# Pet story
print(f"Once upon a time, there was a {pet_type} named {pet_name}.")
print(f"{pet_name} was {pet_age} years old and loved going on adventures.")
print(f"One sunny day, {pet_name} decided to explore the neighborhood and found a magical garden.")
print(f"In the garden, {pet_name} made friends with other animals and played till the sun went down.")
print("What an exciting day it was for " + pet_name + "!")


#Explanation:
#Arithmetic Operations: Basic arithmetic operations are performed and printed.
#Temperature Check: Depending on the temperature value, different messages are printed.
#Weight Conversion: User's input is taken to convert weight from pounds to kilograms or vice versa.
#Fahrenheit to Celsius Conversion: User's input is taken to convert the temperature from Fahrenheit to Celsius.
#Pet Information and Story: User is asked about their pet, and a story involving the pet is generated and printed.
#You can run this code in a Python