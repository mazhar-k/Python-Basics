str1 = list((input("Enter a string:\n")))
str1_cpy = str1.copy()
str1_cpy.reverse()
if str1 == str1_cpy:
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")