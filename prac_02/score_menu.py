"""
display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>
"""
MENU = """(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "G":
        get_score = float(input("Enter score: "))
        while get_score < 0 or get_score > 100:
            print("Invalid score!")
            get_score = float(input("Enter score: "))
        print("Valid Score!")
    elif choice == "P":
        score = float(input("Enter score: "))
        if score < 0 or score > 100:
            print("Invalid score")
        elif score >= 90:
            print("Excellent")
        elif score >= 50:
            print("Passable")
        else:
            print("Bad")
    elif choice == "S":
        score = int(input("Enter score: "))
        print(score * "*")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Farewell")