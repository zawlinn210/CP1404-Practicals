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


def main():
    """Print menu and verify choice"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print("Valid Score!")
        elif choice == "P":
            print(determine_score_status(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    """Get valid score"""
    get_score = float(input("Enter score: "))
    while get_score < 0 or get_score > 100:
        print("Invalid score!")
        get_score = float(input("Enter score: "))
    return int(get_score)


def determine_score_status(score):
    """Determine score status"""
    if score < 0 or score > 100:
        status = "Invalid score"
    elif score >= 90:
        status = "Excellent"
    elif score >= 50:
        status = "Passable"
    else:
        status = "Bad"
    return status


def print_stars(score):
    """Print stars"""
    print(score * "*")


main()
