"""
CP1404 Practical: More Guitars
"""

from prac_07.guitar import Guitar


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()

    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    for guitar in guitars:
        guitars.sort()
        print(guitar)

    name = input("Enter guitar name: ")
    year = int(input("Enter year: "))
    price = float(input("Enter price: "))
    write_to_file(name, price, year)


def write_to_file(name, price, year):
    """Write new guitars to file."""
    with open("guitars.csv", "a") as out_file:
        print(f"{name},{year},{price:.2f}", file=out_file)


main()
