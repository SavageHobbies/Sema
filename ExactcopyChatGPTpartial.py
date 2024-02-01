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

#human code testing

print("1")

i=1
while i <=5:
    print(i)
    i = i +1

b = 1
while b <= 5:
    print(b * '*')
    b = b + 1

names = ["John", "Sean", "Bob", "Sally"]
print(names)
print(names[0])
print(names[-1])
names [0] = "Jon"
print(names)
print(names [0:3])

numbers = [1, 2, 3, 4, 5, 100, 150, 200]
print(150 in numbers)
print(len(numbers))

#End Human Code Testing

#Bard Code Testing

#Here's some cool code I think everyone should learn, added to your existing practice code:
# Generating random passwords
import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

password_length = 12
password = ""

for i in range(password_length):
    category = random.choice([letters, numbers, symbols])
    password += random.choice(category)

print("Your generated password is:", password)

# Text-based adventure game
print("Welcome to the adventure game!")
print("You are standing in a dark forest.")
print("There are two paths ahead: left and right.")

choice = input("Which path do you choose? (left or right) ")

if choice == "left":
    # Continue the adventure with more choices and outcomes
elif choice == "right":
    # Navigate to a different part of the adventure
else:
    print("Invalid choice. Please choose left or right.")


#End Bard Code Testing
    
#Begin Claude Code Testing

# Object Oriented Programming
class Vehicle:
    def __init__(self, make, model, fuel="gas"):
        self.make = make 
        self.model = model
        self.fuel = fuel
        
    def drive(self):
        print("The " + self.make + " " + self.model + " goes vroom!")

car = Vehicle("Toyota", "Camry")
car.drive()

# List Comprehensions 
nums = [1, 2, 3, 4]
squared_nums = [num**2 for num in nums]
print(squared_nums)

# Lambda Functions
double = lambda x: x * 2
print(double(7))

# Map and Filter
cities = ["New York", "Shanghai", "Munich", "Tokyo"]
capitalized_cities = list(map(lambda city: city.title(), cities))
print(capitalized_cities)

long_cities = list(filter(lambda city: len(city) > 5, cities)) 
print(long_cities)

# Decorators
def decorate_message(fun):
    def add_stars(text):
        return "*** " + fun(text) + " ***"
    return add_stars

@decorate_message
def get_text(text):
    return text

print(get_text("Hello World"))

# Context Managers
with open("file.txt") as file:
    data = file.read()
    print(data)   
    #End Claude Code Testing
     