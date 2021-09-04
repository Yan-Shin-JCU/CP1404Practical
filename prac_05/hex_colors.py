"""
CP1404/CP5632 Practical - Suggested Solution
Hexadecimal colour lookup
"""

HEX_CODES = {"Brown": "#a52a2a", "Burlywood": "#deb887",
             "AntiqueWhite": "#faebd7", "DarkGoldenRod": "#b8860b",
             "Aquamarine": "#7fffd4", "DarkOrange": "#ff8c00",
             "CadetBlue": "#5f9ea0", "Chocolate": "#d2691e",
             "CornFlowerBlue": "#6495edb", "Beige": "#f5f5dc"}

color_name = input("Enter name of the color: ")
while color_name != "":
    print("The hex code for {} is {}".format(color_name, HEX_CODES.get(color_name)))
    color_name = input("Enter name of the color: ")
