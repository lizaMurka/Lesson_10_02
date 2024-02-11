num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

choice = input("Enter 1 for maximum, 2 for minimum, 3 for average: ")

if choice == "1":
    result = max(num1, num2, num3)
elif choice == "2":
    result = min(num1, num2, num3)
elif choice == "3":
    result = (num1 + num2 + num3) / 3
else:
    print("Wrong choice!")
    result = None

if result is not None:
    print("Result:", result)