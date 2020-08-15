list1 = [0, 2, 4, 6, 8]
list2 = [1, 3, 5, 7, 9]
list3 = list1 + list2
sum = 0
for x in range(0, len(list3)):
    sum += list3[x]
print("Sum of elements of list1 and list2 is: ", sum)