n = int(input("Enter a number:\n"))
fact = 1
while n!=0:
    fact *= n
    n -= 1
print("Factorial of the number is: ", fact)
