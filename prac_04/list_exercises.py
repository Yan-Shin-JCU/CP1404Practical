def main():
    num_list = get_num()
    first_last(num_list)
    print(num_list)
    min_max(num_list)
    average(num_list)


def get_num():
    count = 0
    num_list = []
    while count < 5:
        num_input = int(input('Number: '))
        num_list.append(num_input)
        count += 1
    return num_list


def first_last(num_list):
    print('The first number is {}'.format(num_list[0]))
    print('The last number is {}'.format(num_list[-1]))


def min_max(num_list):
    print('The smallest number is {}'.format(min(num_list)))
    print('The largest number is {}'.format(max(num_list)))


def average(num_list):
    print('The average number is {}'.format(sum(num_list) / len(num_list)))


def name_check():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn',
                 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    input_name = input('Type username: ')
    if input_name in usernames:
        print('Access Granted')
    else:
        print('Access Denied')


name_check()

main()
