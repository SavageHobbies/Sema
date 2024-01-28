print(10 / 3)
print(10 // 3)

print(10 % 3)

print(10 ** 3)

print(10 + 3)

x = 10
x = x + 3
x += 3
temperature = 35

if temperature >= 30:
    print("It's hot")
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
    print("Wear warm clothes")

weight = int(input("What is your Weight?"))
unit =input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.453592
    print("Your Weight in Kg is " + str(converted))

elif input == "L":
    converted = weight * 0.453592
    print("Your Weight in Lbsis is " + str(converted))
else:
    print("Invalid input")

