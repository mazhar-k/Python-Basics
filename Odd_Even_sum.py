even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
result = []
for e,o in zip(even,odd):
    temp = e + o
    result.append(temp)
print(result)
