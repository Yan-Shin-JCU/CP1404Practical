try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:  # # To fix this just add a loop that runs until you put in a non zero denominator
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:  # # Value error occurs when the input are not numbers
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:  # # ZeroDivisionError occurs when denominator is zero
    print("Cannot divide by zero!")
print("Finished.")
