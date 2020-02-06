import json
import os
import re


def print_menu():
    print("################################")
    print("### Welcome to PhoneBook CLI ###")
    print("################################")
    print("1. Print Phone Number  ")
    print("2. Search By Name of Phone Number ")
    print("3. Add a Phone Number  ")
    print("4. Load File  ")
    print("5. Delete the Phone Book dictionary")
    print("6. Quit ")


def print_PhoneNo():
    if (os.stat("phonebook.json").st_size == 0) is True:
        print("File is empty")
    else:
        x = loadFile()
        for i in x:
            print("Phone number of '%s' is '%s' " % (i, x[i]))


def add_PhoneNo():
    regexPhoneNo = re.compile(
        "^(?:\+?(61))? ?(?:\((?=.*\)))?(0?[2-57-8])\)? ?(\d\d(?:[- ](?=\d{3})|(?!\d\d[- ]?\d[- ]))\d\d[- ]?\d[- ]?\d{"
        "3})$")
    # ask user how many people to add?
    totalNo = int(input("How many people would you like to add? : "))
    # adding elements to the dictionary items
    for i in range(1, totalNo + 1):
        # run until user inputs correct phone number
        while True:
            data = input("Enter the " + str(i) + " Phone Number followed by first_name & number separated by ':' ")
            temp = data.split(":")
            if regexPhoneNo.match(temp[1]):
                phoneBook[temp[0].lower()] = str(temp[1])
                break
            else:
                print("Enter valid phone number")

    # checking if the file is empty, will return False if the file isn't empty
    if (os.stat("phonebook.json").st_size == 0) is True:
        with open("phonebook.json", "w") as json_File:
            json.dump(phoneBook, json_File, indent=2, sort_keys=True)
    else:
        with open("phonebook.json") as jsonFile1:
            x = json.load(jsonFile1)
        x.update(phoneBook)  # updates the phonebook found in the json file
        with open("phonebook.json", "w") as jsonFile2:
            json.dump(x, jsonFile2, indent=2, sort_keys=True)


# json string decoding, object-> dict
def loadFile():
    with open("phonebook.json") as jsonFile1:
        x = json.load(jsonFile1)
        return x


# search in the dictionary file
def searchPhoneNo():
    name = input("Enter the name of the person to search: ").lower()
    nameToSearch = loadFile()
    if name in nameToSearch:
        print("Phone number of '%s' is '%d' " % (name, nameToSearch[name]))


# function to delete the whole content of the file
def deletePhoneBook():
    x = loadFile()
    for i in list(x):
        del (x[i])
    with open("phonebook.json", "w") as jsonFile2:
        json.dump(x, jsonFile2)


def user_Input():
    userInput = int(input("Please choose the number you would like to do? : "))
    while userInput != " ":
        if userInput == 2:
            searchPhoneNo()
        elif userInput == 3:
            add_PhoneNo()
        elif userInput == 1:
            print_PhoneNo()
        elif userInput == 5:
            deletePhoneBook()


phoneBook = dict()
print_menu()
user_Input()

# add_PhoneNo()
# print_PhoneNo()
# deletePhoneBook()
# searchPhoneNo()
