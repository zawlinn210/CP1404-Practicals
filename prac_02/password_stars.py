def main():
    """Get password and print asterisks"""
    password = get_password()
    show_asterisks(password)


def get_password():
    """Get password"""
    password = input("Enter password: ")
    while len(password) < 4:
        print("Password Too Short!")
        password = input("Enter password: ")
    return password


def show_asterisks(password):
    """Print asterisks"""
    print(len(password) * "*")


main()
