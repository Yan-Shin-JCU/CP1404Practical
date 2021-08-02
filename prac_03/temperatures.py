"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def CelsiusToFahrenheit():

    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def FahrenheitToCelsius():

    fahrenheit = float(input("fahrenheit: "))
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


while choice != "Q":
    if choice == "C":
        print("Result: {:.2f} F".format(CelsiusToFahrenheit()))
    elif choice == "F":

        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.

        print("Result: {:.2f} F".format(FahrenheitToCelsius()))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")