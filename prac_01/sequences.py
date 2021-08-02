print('i)Show the even numbers from x to y\nii)Show the odd numbers from x to y\n'
      'iii)Show the squares from x to y\niv)Exit the program')
menu_choice = input('>>> ')
while menu_choice != 'iv':
    if menu_choice == 'i':
        range_start = int(input('Enter starting number: '))
        range_end = int(input('Enter ending number: '))
        for i in range(range_start, range_end):
            if i % 2 == 0:
                print(i)
        print('i)Show the even numbers from x to y\nii)Show the odd numbers from x to y\n'
              'iii)Show the squares from x to y\niv)Exit the program')
        menu_choice = input('>>> ')

    elif menu_choice == 'ii':
        range_start = int(input('Enter starting number: '))
        range_end = int(input('Enter ending number: '))
        for i in range(range_start, range_end):
            if i % 2 != 0:
                print(i)
        print('i)Show the even numbers from x to y\nii)Show the odd numbers from x to y\n'
              'iii)Show the squares from x to y\niv)Exit the program')
        menu_choice = input('>>> ')

    elif menu_choice == 'iii':
        range_start = int(input('Enter starting number: '))
        range_end = int(input('Enter ending number: '))
        for i in range(range_start, range_end):
            print(i * i)
        print('i)Show the even numbers from x to y\nii)Show the odd numbers from x to y\n'
              'iii)Show the squares from x to y\niv)Exit the program')
        menu_choice = input('>>> ')

    else:
        print('Invalid choice')
        print('i)Show the even numbers from x to y\nii)Show the odd numbers from x to y\n'
              'iii)Show the squares from x to y\niv)Exit the program')
        menu_choice = input('>>> ')
