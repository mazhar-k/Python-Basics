cars=['BMW', 'Audi', 'MercBenz', 'Hyundai']
cars_cpy=cars.copy()
cars_cpy.reverse()
# 1st option
print(cars_cpy[2:])
cars.pop(1)
cars[2]="Renault"
# 2nd option
print(cars)
cars.append("Hyundai")
for x in cars:
    # 3rd option
    print(x, end=" ")
# 4th option
print('\n', len(cars))
