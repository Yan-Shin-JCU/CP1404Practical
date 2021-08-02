def main():
    input_pass = get_password()
    print_asterisk(input_pass)


def print_asterisk(input_pass):
    print(len(input_pass) * '*')


def get_password():
    input_pass = input('Type Password: ')
    while len(input_pass) <= 1:
        input_pass = input('Type Password: ')
    return input_pass


main()
