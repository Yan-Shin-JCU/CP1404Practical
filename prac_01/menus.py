user_name = input('Enter Name: ')
print('(H)ello\n(G)oodbye\n(Q)uit')
user_choice = input('>>> ')

while user_choice != 'Q':
    if user_choice == 'H':
        print('Hello {name}'.format(name=user_name))
        print('(H)ello\n(G)oodbye\n(Q)uit')
        user_choice = input('>>> ')
    elif user_choice == 'G':
        print('Goodbye {name}'.format(name=user_name))
        print('(H)ello\n(G)oodbye\n(Q)uit')
        user_choice = input('>>> ')
    else:
        print('Invalid choice')
        print('Goodbye {name}'.format(name=user_name))
        print('(H)ello\n(G)oodbye\n(Q)uit')
        user_choice = input('>>> ')