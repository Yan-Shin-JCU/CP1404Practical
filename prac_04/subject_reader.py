"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data_list = []
    data = get_data(data_list)
    print(data)


def get_data(data_list):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    count = 0
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data_list.append(parts)
        print_data(count, data_list)

    return data_list

    input_file.close()


def print_data(count, data_list):
    print("----------")
    print(
        '{} is taught by {} and has {} students'.format(data_list[count][0], data_list[count][1], data_list[count][2]))
    count += 1


main()
