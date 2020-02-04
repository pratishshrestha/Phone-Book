def print_menu():
    print("################################")
    print("### Welcome to PhoneBook CLI ###")
    print("################################")
    print("1. Print Phone Number  ")
    print("2. Search By Name of Phone Number ")
    print("3. Add a Phone Number  ")
    print("4. Load File  ")
    print("5. Quit ")


def print_PhoneNo():
    try:
        file = open("phonebook.txt", "r")
        print(file.read())
        file.close()
    except OSError:
        print("Error No Such Files to Read")


def add_PhoneNo():
    file = open("phonebook.txt", "w+")
    phoneBook = dict()
    totalNo = int(input("How many people would you like to add? : "))
    for i in range(1, totalNo + 1):
        print("Enter the " + str(i) + " Phone Number followed by name & number separated by ':' ")
        



print_menu()
print_PhoneNo()
