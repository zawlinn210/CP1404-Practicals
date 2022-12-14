COLOR_TO_CODE = {"Amaranth": "	#e52b50", "Amber": "#ffbf00", "Barn Red": "#7c0a02", "Banana Yellow": "#ffe135",
                 "Carmine": "#960018", "Carnelian": "#b31b1b", "Deep Saffron": "#ff9933", "Firebrick": "#b22222",
                 "Imperial Red": "#ed2939", "Oxblood": "#4a0000"}
color_name = input("Enter color name: ").title()
while color_name != "":
    if color_name in COLOR_TO_CODE:
        print("The hexadecimal colour code of", color_name, "is", COLOR_TO_CODE[color_name])
    else:
        print(f"There is no hexadecimal color code for {color_name}")
    color_name = input("Enter color name: ").title()