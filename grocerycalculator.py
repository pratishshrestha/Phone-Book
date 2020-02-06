from datetime import date

print("#####################################################")
print("#####################################################")
print("---------- Welcome to Grocery Calculator ------------")
print("#####################################################")
print("#####################################################")
print("\n")
print("How many people would you like to add?")

totalPeople = int(input())  # ask for the total number of people

# print("Today's date: ", date.today()) #print's today's date

peopleList = dict()
print("Enter the names of each: ")
for i in range(totalPeople):
    name = input().lower()
    peopleList[name] = 0  # Setting Total Expenses for now to zero

while True:  # run until you find the correct user
    print("Who are you: ")

    askUser = input().lower()  # ask which user

    if askUser in peopleList.keys():  # check if user is in dictionary
        print(askUser + " activated")
        print("How many expense would you like to add? ")
        numberofExpense = int(input())
        for i in range(numberofExpense):  # do the sum of no. of expense done by particular user
            expense = float(input("What is the expense on " + str(date.today()) + " "))
            expense += peopleList[askUser]
            peopleList[askUser] = expense
        nextUser = int(input("Is there any other user you would like to add? If yes press 1 and press 0 for no "))
        if nextUser == 0:
            break
        else:
            print("Provide your name on asking who are you again?")
    else:
        print("Enter a valid name from the list: ")
        print(*sorted(peopleList.keys()), sep='\n')  # removal of dict_keys and printing in sorted manner
        """# Displaying the dictionary
            for key, value in class_list.items():
            print('Name: {}, Score: {}'.format(key, value))"""

totalExpense = sum(peopleList.values())  # total expense in grocery

expenseEachHead = totalExpense / totalPeople  # expense of each head

for i in peopleList:  # loop to findout the difference on who owes how much amount
    result = peopleList[i] - expenseEachHead
    peopleList[i] = result

print(peopleList)
highestSpenderName = max(peopleList, key=lambda key: peopleList[key])
print(
    highestSpenderName + " is the highest spender in grocery bills")  # copied from stackoverflow to figure out the
# maximum spender also if two amount is max such as 40 and 40 it will return the first keys
maxHighestSpenderNo = max(peopleList.values())
peopleList = {key: val for key, val in peopleList.items() if
              val != maxHighestSpenderNo}  # updated list with deletion of the item of highest number
print(peopleList)
x = 0  # its because we cannot iterate over list(peopleList)[i] as it will produce error
for i in peopleList:

    if peopleList[i] < 0:
        print(str(list(peopleList)[x]) + " owes " + highestSpenderName + " amount " + str(
            "%.2f" % abs(peopleList[i])))  # "%.2f" is for two decimal point
        x += 1
    else:
        print(highestSpenderName + " owes " + str(list(peopleList)[x]) + " amount " + str("%.2f" % peopleList[i]))
        x += 1
