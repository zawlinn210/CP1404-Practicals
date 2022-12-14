"""
Emails
Estimate: 20 minutes
Actual:   23 minutes
"""


def main():
    """Create dictionary of email to name"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(name, f"({email})")


def get_name(email):
    """Extract name from email"""
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


main()
