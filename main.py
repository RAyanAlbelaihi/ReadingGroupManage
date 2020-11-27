from datetime import date

import numpy
import pandas

from Members import members

members_file = open('members_file.txt', 'a+')
books_file = open('books_file.txt', 'a+')
history_file = open('history_file.txt', 'a+')
today = date.today()

print(
    'choice a number:\n 1.Add Member \n 2.Member b􏰁􏰁ook􏰂􏰃 information \n 3.reader activity \n 4.statistical reports')
choice = input('')
def Add_Member():
    name = ''
    while name != "0":
        print('enter 0 to end the loop')
        name = input("enter your name:")
        if name != "0":
            email = input("enter your email:")
            number = input("enter your number:")
            group = input("enter group name:")
            members_file.writelines(name + "," + email + "," + number + ",group:" + group + "\n")

            p3 = members(name, number, email, group)
            p3.myfun()

def member_Book_Information():
    Titles_of_books = input("enter Titles of the books:")
    Number_of_pages = input("enter Number of pages for each book:")
    Category = input("enter Category of book:")
    books_file.writelines(Titles_of_books + "," + Number_of_pages + "," + Category + "\n")

def reader_Activity():
    Name = input('name:')
    Book = input('book:')
    Group = input('Group:')
    Time = today.strftime("%B")
    history_file.writelines(Name + "," + Book + ",group:" + Group + "," + Time + "\n")
    history_file.seek(0)
    print(history_file.read())

def statistical_Reports():
    print(
        'choice a number:\n1.Number of books read by the whole group members\n2.Number of pages read by the whole '
        'group members\n3.Ranking of books categories mostly read by the group members\n4.Ranking of group members '
        'based on number of books read\n5.Ranking of group members based on number of pages read')
    choiceInput = input('')
    if choiceInput == '1':
        history_file.seek(0)
        resultFullHistory = history_file.read().splitlines()
        filterResult = []
        GroupName = input('which group do you want?')
        for element in resultFullHistory:
            if element.find("group:" + GroupName) != -1:
                filterResult.append(element)

        print(len(filterResult), 'books')
    if choiceInput == '2':
        history_file.seek(0)
        books_file.seek(0)
        resultFullHistory = history_file.read().splitlines()
        resultFullBooks = books_file.read().splitlines()
        filterResult = []
        filterBooks = []
        groupPagesRead = 0
        GroupName = input('which group do you want?')
        month = input('which month do you want?')
        for element in resultFullHistory:
            if (element.find("group:" + GroupName) != -1) and (element.find(month) != -1):
                filterResult.append(element)
        for element in filterResult:
            temp = element.split(',')
            filterBooks.append(temp[1])
        for element in filterBooks:
            for element2 in resultFullBooks:
                temp = element2.split(',')
                if element == temp[0]:
                    groupPagesRead = groupPagesRead + int(temp[1])

        print(groupPagesRead, 'pages read by the group')

    if choiceInput == '3':
        history_file.seek(0)
        books_file.seek(0)
        resultFullHistory = history_file.read().splitlines()
        resultFullBooks = books_file.read().splitlines()
        GroupName = input('which group do you want?')
        month = input('which month do you want?')
        filterBooks = []
        categoriesRead = []
        filterResult = []
        for element in resultFullHistory:
            if (element.find("group:" + GroupName) != -1) and (element.find(month) != -1):
                filterResult.append(element)
        for element in filterResult:
            temp = element.split(',')
            filterBooks.append(temp[1])
        for element in filterBooks:
            for element2 in resultFullBooks:
                temp = element2.split(',')
                if element == temp[0]:
                    categoriesRead.append(temp[2])
        uniqueCatName, catCounts = numpy.unique(categoriesRead, return_counts=True)

        listOfUniqueCat = zip(uniqueCatName, catCounts)
        print("Group " + GroupName + " have read in " + month + ": \n")

        for element in listOfUniqueCat:
            print(str(element[0]) + " " + str(element[1]) + " times \n")

    if choiceInput == '4':
        history_file.seek(0)
        resultFullHistory = history_file.read().splitlines()
        GroupName = input('which group do you want?')
        month = input('which month do you want?')
        filterResult = []
        filterBooks = []
        filterName = []
        for element in resultFullHistory:
            if (element.find("group:" + GroupName) != -1) and (element.find(month) != -1):
                filterResult.append(element)
        for element in filterResult:
            temp = element.split(',')
            filterBooks.append(temp[0])
        for element in filterBooks:
            for element2 in resultFullHistory:
                temp = element2.split(',')
                if element == temp[0]:
                    filterName.append(temp[1])
        uniqueCatName, catCounts = numpy.unique(filterBooks, return_counts=True)

        listOfUniqueCat = zip(uniqueCatName, catCounts)
        print("Group " + GroupName + " have read in " + month + ": \n")

        listToBeSorted = []

        for element in listOfUniqueCat:
            temp = [element[0], element[1]]
            listToBeSorted.append(temp)

        listToBeSorted.sort(reverse=True, key=lambda x: x[1])

        for element in listToBeSorted:
            print(str(element[0]) + " " + str(element[1]) + " books \n")

    if choiceInput == '5':
        history_file.seek(0)
        books_file.seek(0)
        resultFullHistory = history_file.read().splitlines()
        resultFullBooks = books_file.read().splitlines()
        filterResult = []
        pagesReadByGroup = []

        GroupName = input('which group do you want?')
        month = input('which month do you want?')
        for element in resultFullHistory:
            if (element.find("group:" + GroupName) != -1) and (element.find(month) != -1):
                filterResult.append(element)

        for element in filterResult:
            temp1 = element.split(',')
            for element2 in resultFullBooks:
                temp2 = element2.split(',')
                if temp1[1] == temp2[0]:
                    tmpString = [temp1[0], int(temp2[1])]
                    pagesReadByGroup.append(tmpString)
        groupByTemp = pandas.DataFrame(pagesReadByGroup) \
            .groupby(0, as_index=False) \
            .sum() \
            .reset_index()
        res = groupByTemp[[0, 1]].values
        sortingTemp = []

        for element in res:
            temp = [element[0], element[1]]
            sortingTemp.append(temp)

        sortingTemp.sort(reverse=True, key=lambda x: x[1])
        for element in sortingTemp:
            print(element[0] + " have read " + str(element[1]) + " pages.\n")


if choice == '1':
    print(Add_Member())

if choice == '2':
    print(member_Book_Information())

if choice == '3':
    print(reader_Activity())

if choice == '4':
    print(statistical_Reports())

books_file.close()
members_file.close()
