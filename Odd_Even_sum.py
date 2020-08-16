even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
result = []
for e,o in zip(even,odd):
    tem = e + o
    result.append(tem)
print(result)
