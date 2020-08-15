a = int(input("Enter first number\n"))
b = int(input("Enter second number\n"))
operation = input("""Choose one of the following operations:
                  Addition
                  Subtraction
                  Multiplication
                  Division
                  Modulus\n""")
if "Addition" in operation:
    print("result: " + str(a + b))
elif "Subtraction" in operation:
    print("result: " + str(a + b))
elif "Multiplication" in operation:
    print("result: " + str(a + b))
elif "Division" in operation:
    print("result: " + str(a + b))
elif "Modulus" in operation:
    print("result: " + str(a + b))
else:
    print("Option not valid! Try again")
