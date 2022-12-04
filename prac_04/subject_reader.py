"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Get subject data"""
    data = get_data()
    print(data)
    display_subject(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subject(data):
    """Display subject data"""
    for subjects in data:
        print(f"{subjects[0]} is taught by {subjects[1]:12} and has {subjects[2]:3} students")


main()
