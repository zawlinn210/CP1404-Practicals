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
            filename = input("Enter filename: ")
            if filename != "":
                try:
                    projects = get_file(filename)
                    print(projects)
                except FileNotFoundError:
                    print("Invalid Filename!")

        elif choice == "S":
            filename = input("Enter filename to be saved: ")
            save_file(filename, projects)

        elif choice == "D":
            complete_project, incomplete_project = check_project(projects)
            print("Incomplete projects: ")
            incomplete_project.sort()
            display_project(incomplete_project)
            print("")
            print("Completed projects: ")
            complete_project.sort()
            display_project(complete_project)

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


def save_file(filename, projects):
    with open(filename, "w") as out_file:
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost}\t{project.completion}",
                  file=out_file)


def display_project(projects):
    for number, project in enumerate(projects):
        print(f"{number + 1} {project}")


def check_project(projects):
    complete_project = []
    incomplete_project = []
    for project in projects:
        if project.is_complete():
            complete_project.append(project)
            complete_project.sort()
        else:
            incomplete_project.append(project)
            incomplete_project.sort()
    return complete_project, incomplete_project


main()