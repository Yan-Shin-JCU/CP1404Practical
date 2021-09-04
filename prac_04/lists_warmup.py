
# numbers[0] 3
# numbers[-1] 2
# numbers[3] 1
# numbers[:-1] 3, 1, 4, 1, 5, 9
# numbers[3:4] 1
# 5 in numbers numbers.append(5)
# 7 in numbers numbers.append(7)
# "3" in numbers numbers.append('3')
# numbers + [6, 5, 3] [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0] = 'ten'
print(numbers)

numbers[-1] = 1
print(numbers)

print(numbers[2:])
print(9 in numbers)



