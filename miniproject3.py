adminDictionary = {"admin": "123"}  # credentials of admin
studentDictionary = {"Ahmet": "1234", "Ayse": "4567"}  # credentials of students

adminMenuDictionary = {1: "List books", 2: "Create a book", 3: "Clean a book", 4: "Search for a book" , 5: "Change number of copies of book by id ",
                       6: "Show students borrowed a book by id", 7: "List Users by id", 8: "Create User ", 9: "Delete User", 10: "Exit"}  # admin menu

studentMenuDictionary = {1: "Search for a book", 2:"Add a book to my books list ", 3: "Delete a book from my books list", 4: "Show my borrowed books", 5: "Exit"} #student menu

bookDictionary={"Biology":["001",['Alice', 'Bob'], 2, "Ayse", "Ahmet"], "Chemistry":["002",['Alice'], 1]}  # book information

newDictionary = {}  # contains credentials of admin and students.
newDictionary.update(studentDictionary)
newDictionary.update(adminDictionary)

print("****​Welcome to Library Management System​****")
print("Please provide login information")


def checkingUserCredentials(studentChoice):  # decides if the user is admin or a student.
    id = input("Id:")
    if id in list(newDictionary):  # the id is in new dictionary means user entered a valid id,
        password = input("Password:")  # then asks password.
        if password != newDictionary[id]:  # if password isn't valid,
            print("Invalid id or password please try again ")
            checkingUserCredentials(studentChoice)  # turns to the beginning and asks id and password again.

        # after id and password matched, checks if the user is admin or a student.
        if id != "admin":  # checks if the user is student and the password matches that student.
            if password != studentDictionary[id]:  # if password doesn't match student,
                print("Invalid id or password please try again ")
                checkingUserCredentials(studentChoice)  # asks credentials again.
            else:  # if password matches student,
                print("Successfully logged in!")  # student logs in,
                studentMenu(id)  # and students menu is shown.
        elif id == "admin":  # checks if the user is admin and the password matches admin.
            if password != adminDictionary[id]:  # if password doesn't match admin,
                print("Invalid id or password please try again ")
                checkingUserCredentials(studentChoice)  # asks credentials again.
            else:  # if password matches admin,
                print("Successfully logged in!")  # admin logs in,
                print("Welcome Admin! What do you want to do?")
                adminMenu(id, studentChoice)   # and admin menu is shown.
    else:
        print("Invalid id or password please try again ")  # if the id that user entered isn't valid,
        checkingUserCredentials(studentChoice)  # asks credentials again.


def print_list_of_books():  # prints list of books.
    bookNumber = 1  # at first, number at the beginning of book is 1,
    print("*** List of Books  ***")
    for key in bookDictionary:
        print(str(bookNumber) + ". " + "Book id: " + str(bookDictionary[key][0]) + ", Book Name: " + str(
            key) + ", Book Authors: " + str(bookDictionary[key][1]) +
              ", Number of Copies: " + str(bookDictionary[key][2]))
        bookNumber += 1  # number at the beginning of book increases by 1 when book number increases.


def take_another_book_id_for_new_book(added_book, studentChoice):  # if id that user entered exists, asks another id and adds book which has id that user entered.
    id_of_new_book = input("What is the id that you want to give for " + added_book + " book?:")
    for key in bookDictionary:
        if id_of_new_book == bookDictionary[key][0]:  # if id that user entered exists,
            print("This id is already taken by another book, please provide another input id")
            take_another_book_id_for_new_book(added_book, studentChoice)  #  asks another id .
    author_of_new_book = input("What is/are the author(s) of " + added_book + " book?:")
    copies_of_new_book = input("How many copies you have for " + added_book + " book?:")
    are_you_sure = input("Are you sure?[Y/N]")
    if are_you_sure == "Y" or "y":  # adds book by updating book dictionary.
        bookDictionary.update({added_book: [id_of_new_book, [author_of_new_book], copies_of_new_book]})  # adds book by updating book dictionary.
        print("The following book has been added to your collection:")  # writes added book.
        print("Book id: " + str(bookDictionary[added_book][0]) + ", Book Name: " + str(added_book) +
              ", Book Authors: " + str(bookDictionary[added_book][1]) + ", Number of Copies: " + str(
            bookDictionary[added_book][2]))
        adminMenu(id, studentChoice)


def ask_for_valid_id_to_delete_book(studentChoice):  # asks id to admin and deletes the book which has id that admin entered.
    id_of_deleted_book = input("What is the id of the book that you want to delete,(Enter 0 to go to main menu)?:")
    if int(id_of_deleted_book) == 0:  # if user enters 0,
        adminMenu(id, studentChoice)  # turns to main menu.
    for key in list(bookDictionary):
        if bookDictionary[key][0]==id_of_deleted_book:
            print("The following book has been deleted:")  # prints deleted book.
            print("Book id: " + str(bookDictionary[key][0]) + ", Book Name: " + str(key) +
                  ", Book Authors: " + str(bookDictionary[key][1]) + ", Number of Copies: " + str(
                bookDictionary[key][2]))
            del bookDictionary[key]  # deletes the book.
            adminMenu(id, studentChoice)


def valid_book_or_author_to_search(id, studentChoice):  # when user wants to search a book, provides searching by entering the book's or author of the book's name.
    book_or_author_name = input("Enter book name or author name to search ,(Enter 0 to go to main menu)?:")
    if book_or_author_name == "0":  # if user enters 0,
        if id != "admin":  # if user isn't admin, means s/he is a student,
            studentMenu(id)  # shows student menu.
        else:  # if user is admin,
            adminMenu(id, studentChoice)  # shows admin menu.



def try_a_large_number(id_of_changed_book, studentChoice):  # when admin wants to change the number of copies of a book,
    new_value_of_copies = input("Enter the new value for the no of copies:")  # asks the new value of the number of copies.
    for key in bookDictionary:  # if the number of users that hold the book is more than new copy value,
        if bookDictionary[key][0] == id_of_changed_book:
            if len(bookDictionary[key]) - 3 > int(new_value_of_copies):
                print(str(len(bookDictionary[key]) - 3) + " user(s) is/are holding the book, try a larger number! ")  # warns the admin,
                try_a_large_number(id_of_changed_book, studentChoice)  # asks another value.
            else:  # if there is no problem,
                for key in bookDictionary:
                    if bookDictionary[key][0] == id_of_changed_book:
                        print("The following book has been updated: ")
                        bookDictionary[key][2] = int(new_value_of_copies)  # changes the number of copies of the book that admin wanted to.
                        print("Book id: " + str(bookDictionary[key][0]) + ", Book Name: " + str(key) +
                              ", Book Authors: " + str(bookDictionary[key][1]) + ", Number of Copies: " + str(
                            bookDictionary[key][2]))
                        adminMenu(id, studentChoice)


def delete_user(studentChoice):  # asks admin which user admin wants to delete and deletes that user.
    student_to_be_deleted = input("Which user do you want to delete:")  # asks admin which student s/he wants to delete.
    for key in studentDictionary:
        if key == student_to_be_deleted:
            print(key + " is deleted")
            del studentDictionary[key]  # deletes the student from the student dictionary.
            adminMenu(id, studentChoice)
        else:  # if the name that admin enters isn't valid,
            print("Enter valid user name!")  # warns admin,
            delete_user(studentChoice)  # asks name of user to delete again.


def adminMenu(id, studentChoice):  # main menu for admin.  # this menu is shown at the and of all choices.
    for item in adminMenuDictionary:  # writes admin menu options.
        print(str(item) + "- " +adminMenuDictionary[item])
    choice = input("Your choice:")
    if int(choice) == 1:  # if choice is 1,
        print_list_of_books()  # prints list of the books.
        adminMenu(id, studentChoice)
    elif int(choice) == 2:  # if choice is 2, asks name of the book that admin wants to add,
        added_book = input("What is the name of the book that you want to add?:")
        take_another_book_id_for_new_book(added_book, studentChoice)  # if id that user entered exists,
                                                       # asks another id and adds book which has id that user entered.
    elif int(choice) == 3:  # if choice is 3,
        print_list_of_books()  # prints the list of the books,
        ask_for_valid_id_to_delete_book(studentChoice)  # asks the id to the user and deletes the book which has id that user entered.
    elif int(choice) == 4:  # if choice is 4,
        valid_book_or_author_to_search(id, studentChoice)  # when user wants to search a book, provides searching by entering the book's or author of the book's name.
        adminMenu(id, studentChoice)
    elif int(choice) == 5:  # if choice is 5,
        print_list_of_books()  # prints the list of the books.
        id_of_changed_book = input(
            "What is the id of the book for the change ?(Enter 0 to go to main menu):")  # asks the id of the book that
                                                                                         # admin wants to change number of copies.
        if int(id_of_changed_book) == 0:  # if admin enters 0,
            adminMenu(id, studentChoice)  # turns to main menu.
        try_a_large_number(id_of_changed_book, studentChoice)  # asks the new value of the number of copies and changes it.
    elif int(choice) == 6:  # if choice is 6,
        id_of_showed_book = input("What is the id of the book that you want to show, (Enter 0 to go to main menu)?:")  # asks the id of the book admin wants to show
                                                                                                                       # the students borrowed that book.
        if int(id_of_showed_book) == 0:  # if admin enters 0,
            adminMenu(id, studentChoice)  # turns to the main menu.
        for key in bookDictionary:  # else, writes the students borrow that book.
            if id_of_showed_book == bookDictionary[key][0]:
                n = 3
                for i in range(len(bookDictionary[key])-3):
                    print("-"+bookDictionary[key][n])
                    n += 1
                adminMenu(id, studentChoice)
    elif int(choice) == 7:  # if choice is 7,
        print("*** Current Users *** ")
        userNumber = 1
        for key in studentDictionary:  # lists the students,
            print(str(userNumber) + "-" + key)
            userNumber += 1
        adminMenu(id, studentChoice)
    elif int(choice) == 8:  # if choice is 8, asks user the credentials that admin wants to create.
        name_of_new_user = input("What is the name of the user that you want to create?")
        password_of_new_user = input("What is the password for the new account?")
        studentDictionary.update({name_of_new_user: password_of_new_user})  # adds new user to the student dictionary by updating.
        newDictionary.update(studentDictionary)  # because of updating the student dictionary, the new dictionary should be updated too.
        print("The following user has been added: ")
        print("Name: " + name_of_new_user + ", " + "Password: " + studentDictionary[name_of_new_user])  # writes new user's name and id.
        adminMenu(id, studentChoice)
    elif int(choice) == 9:  # if choice is 9,
        print("*** Current Users *** ")  # prints current users in the student dictionary.
        userNumber = 1
        for key in studentDictionary:
            print(str(userNumber) + "-" + key)
            userNumber += 1
        delete_user(studentChoice)  # asks admin which user admin wants to delete and deletes that user.
    elif int(choice) == 10:  # if choice is 10,
        print("****​Welcome to Library Management System​****")
        print("Please provide login information")
        checkingUserCredentials(studentChoice)  # returns to the very beginning.


def a_book_student_wants_to_add(id):  # adds the book to student's book list that student wants.
    id_of_the_book_added = input("What is the id of a book that you want to add (Enter 0 to go to main menu)?")  # asks the id of the book which is wanted to add.
    if int(id_of_the_book_added) == 0:  # if student enters 0,
        studentMenu(id)  # student menu is shown.
    for key in bookDictionary:
        if id_of_the_book_added == bookDictionary[key][0]:
            if id in bookDictionary[key]:  # if the book that student wants is already in his/her book list,
                print("This book is already in your profile, please choose another book")
                a_book_student_wants_to_add(id)  # asks id of the book again.
            elif bookDictionary[key][2] == 0:  # if number of copies of that book is zero,
                print("There is no available copy, please choose another book")
                a_book_student_wants_to_add(id)  # asks for another book id.
            else:  # if there is no problem
                print("The following book has been added to your profile: ")  # writes the book which is added.
                print("Book id: " + str(bookDictionary[key][0]) + ", Book Name: " + str(key) +
                      ", Book Authors: " + str(bookDictionary[key][1]) + ", Number of Copies: " + str(
                    bookDictionary[key][2]))
                bookDictionary[key].append(id)  # adds the student to the list of book which is selected in book dictionary.
                studentMenu(id)


def studentMenu(id):  # main function for student menu. # this menu is shown at the and of all choices.
    print("Welcome " + id + " what do you want to do ?")
    for item in studentMenuDictionary:  # shows student menu.
        print(str(item)+"-"+studentMenuDictionary[item])
    studentChoice = input("Your choice:")
    if int(studentChoice) == 1:  # if choice is 1,
        valid_book_or_author_to_search(id, studentChoice)  # when user wants to search a book, provides searching by entering the book's or author of the book's name.
        studentMenu(id)
    elif int(studentChoice) == 2:  # if choice is 2,
        print_list_of_books()  # prints the list of the books,
        a_book_student_wants_to_add(id)  # adds the book to student's book list that student wants.
    elif int(studentChoice) == 3:  # if choice is 3,
        print_list_of_books()  # prints the list of the book.
        id_of_the_returned_book = input("What is the id of a book that you want to return (Enter 0 to go to main menu)?:")  # asks the id of the book student wants to return.
        if int(id_of_the_returned_book) == 0:  # if student enters 0,
            studentMenu(id)  # shows student menu.
        for key in list(bookDictionary):  # selects the book student wants to return and deletes it.
            if id_of_the_returned_book == bookDictionary[key][0]:
                print("The following book has been selected:")
                print("Book id: " + str(bookDictionary[key][0]) + ", Book Name: " + str(key) +
                      ", Book Authors: " + str(bookDictionary[key][1]) + ", Number of Copies: " + str(bookDictionary[key][2]))
                ask_sure_or_not = input("Are you sure that you want to return this book ? [Y/N]")
                if ask_sure_or_not == "Y" or "y":
                    bookDictionary[key].remove(id)  # deletes student from that book's values so student doesn't have that book anymore.
                    print("The book has been returned. ")
                    studentMenu(id)
    elif int(studentChoice) == 4:  # if choice is 4,
        print("Your books")
        students_book_number = 1
        for key in bookDictionary:
            if id in bookDictionary[key]:  # shows books that student has.
                print(str(students_book_number)+". Book id: " + str(bookDictionary[key][0]) + ", Book Name: " + str(key) +
                          ", Book Authors: " + str(bookDictionary[key][1]) + ", Number of Copies: " + str(bookDictionary[key][2]))
                students_book_number += 1
        studentMenu(id)
    elif int(studentChoice) == 5:  # if choice is 5,
        print("****​Welcome to Library Management System​****")
        print("Please provide login information")
        checkingUserCredentials(studentChoice)  # returns to the very beginning.


checkingUserCredentials(studentChoice="1")  # makes the id defined for "valid_book_or_author_to_search(id)" function
                                            # and uses it to check if the user is admin or a student to show admin or student menu
                                            # when the user enters zero while searching book.



