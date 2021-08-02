out_file = open("name.txt", "w")
user_name = input("Please type in your name. ")
print(user_name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
user_name = in_file.read().strip()
in_file.close()
print("Your name is", user_name)

in_file = open("numbers.txt", "r")
num1 = int(in_file.readline())
num2 = int(in_file.readline())
in_file.close()
print(num1 + num2)

in_file = open("numbers.txt", "r")
total_sum = 0
for num in in_file:
    total_sum += int(num)
in_file.close()
print(total_sum)
