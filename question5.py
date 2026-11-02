import math_operations

while True:
  print("Select an operation")
  print("To Add type +")
  print("To Subract type -")
  print("To Muliply type *")
  print("To Divide type /")
  print("To Exit type quit")

  operation = input("Enter your choice: ")

  if operation == "quit":
    print("Goodbye")
    break

  if operation in ("+", "-", "*", "/"):
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
    except ValueError:
       print("That is not a valid choice")
       continue

    if operation == "+":
       print(f"Result: {math_operations.add(a, b)}")
    elif operation == "-":
       print(f"Result: {math_operations.subtract(a, b)}")
    elif operation == "*":
       print(f"Result: {math_operations.multiply(a, b)}")
    elif operation == "/":
       try:
          print(f"Result: {math_operations.divide(a, b)}")
       except ZeroDivisionError:
          print("You cannot divide by 0")
  else:
     print("That is not a valid option please select +, -, *, or /")