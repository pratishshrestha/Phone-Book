import json
import os


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
    if (os.stat("phonebook.json").st_size == 0) is True:
        print("File is empty")
    else:
        with open("phonebook.json") as jsonFile1:
            x = json.load(jsonFile1)
        x.update(phoneBook)
        print(x)


def add_PhoneNo():
    # ask user how many people to add?
    totalNo = int(input("How many people would you like to add? : "))
    # adding elements to the dictionary items
    for i in range(1, totalNo + 1):
        data = input("Enter the " + str(i) + " Phone Number followed by first_name & number separated by ':' ")
        temp = data.split(":")
        phoneBook[temp[0].lower()] = int(temp[1])

    # checking if the file is empty, will return False if the file isn't empty
    if (os.stat("phonebook.json").st_size == 0) is True:
        with open("phonebook.json", "w") as json_File:
            json.dump(phoneBook, json_File, indent=2)
    else:
        with open("phonebook.json") as jsonFile1:
            x = json.load(jsonFile1)
        x.update(phoneBook)  # updates the phonebook found in the json file
        with open("phonebook.json", "w") as jsonFile2:
            json.dump(x, jsonFile2, indent=2)


phoneBook = dict()
print_menu()
add_PhoneNo()
print_PhoneNo()
