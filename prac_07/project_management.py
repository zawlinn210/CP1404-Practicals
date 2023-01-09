from prac_07.project import Project

FILENAME = "projects.txt"

def main():
    MENU = "Menu:\n(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n" \
           "(A)dd new project\n(U)pdate project\n(Q)uit"
    projects = get_file(FILENAME)
    print(projects)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice!")
            choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def get_file(filename):
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().replace("\t", ",")
        parts = parts.split(",")
        print(parts)
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()
    return projects








main()