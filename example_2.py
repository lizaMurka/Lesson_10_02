meters = float(input("Keep the number of meters: "))

choice = input("Keep 1 to convert to miles, 2 for inches, 3 for yards: ")

if choice == "1":
  result = meters * 0.000621371
elif choice == "2":
  result = meters * 39.3701
elif choice == "3":
  result = meters * 1.09361
else:
  print("Wrong choice!")

print("Result:", result)