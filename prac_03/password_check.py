
input_pass = input('Type Password: ')
while len(input_pass) <= 1:
    input_pass = input('Type Password: ')
print(len(input_pass) * '*')