from db_connection import *
from prettytable import PrettyTable
import json
import csv


# dictionary to store fetched data
# kind of a session variable like PHP
user_detail = {
    'name': '',
    'email': '',
    'password': ''
}

# CRUD function of student registration system
def sr_system():

    # checking if user is logged in or not
    if  user_detail['name'] != '' and user_detail['email'] != '' and user_detail['password'] != '':

        # sasti c styling nothing else
        print("=================================")
        print("== STUDENT REGISTRATION SYSTEM ==")
        print("=================================")
        print("\n Hello and Welcome to the Application", user_detail['name'], "!")
        print("\nDirections:\n")
        print("1. Type 'a' to Add New Student")
        print("2. Type 'b' to View List of Students")
        print("3. Type 'c' to Edit Student Details")
        print("4. Type 'd' to Delete Student")
        print("5. Type 'e' to Logout")
        print("5. Type 'f' to Download Student's Details")
        print("5. Type 'g' to Register New User")

        # grabbing user's choice
        choice = input("\nEnter your command to proceed:")
        choice = choice.lower()

        # some sort of decision making on user's input
        if choice == 'a':
            # calling add new student function
            add_student()

        elif choice == 'b':
            # calling view list of students function
            view_students()

        elif choice == 'c':
            # calling edit student's details function
            edit_student()

        elif choice == 'd':
            # calling delete student function
            delete_student()

        elif choice == 'e':
            # calling logout function
            logout()

        elif choice == 'f':
            # calling download function
            download()

        elif choice == 'g':
            # calling register function
            register_user()

        else:
            # calling same function while showing a custom error
            print("Please use commands mentioned above only [a, b, c, d]")
            sr_system()
    else:
        authenticate_user()


# adding student to the database function
def add_student():
    # setting value for looping in the same function
    i = 1

    # generating loop on basis of above 'i'
    while i > 0:

        # getting student details and converting to lower case
        student_name = input("\nEnter Student's Name: ")
        subject = input("Enter Student's Subject: ")
        s_name = student_name.title()
        s_subject = subject.title()

        # sql query and values to insert data to the database
        sql_query = "INSERT INTO students (name, class) values (%s, %s)"
        values_to_db = (s_name, s_subject)

        # executing query to send data to the DB
        my_database.execute(sql_query, values_to_db)

        # to save changes this command is used (isse zada is k bare mai kuch nai pata :P)
        db_connection.commit()

        # asking user if he/she wants to add more student or not
        desire = input("\nDo you want to add more student (y/n)?: ").lower()

        # taking decision on the bases of users above input
        if desire == 'y':
            i += 1
        else:
            i = -1

    # if loop ends we'll get back to the main function again
    sr_system()


# view students fetching all from database
def view_students():
    # sql query and values to fetch data from the database
    sql_query = "SELECT * FROM students"
    my_database.execute(sql_query)
    students = my_database.fetchall()

    # using pretty table library to show data
    pretty_table_object = PrettyTable()

    pretty_table_object.field_names = ["Student ID", "Student's Name", "Subject"]

    for student in students:
        pretty_table_object.add_row([student[0], student[1], student[2]])

    students_table = pretty_table_object.get_string()
    print("\n"+students_table)

    # asking user if he/she wants to go back to main function
    desire = input("\nDo you want jump back (y/n)?: ")
    desire = desire.lower()

    # taking decision on the bases of users above input
    if desire == 'y':
        sr_system()
    else:
        view_students()


# edit student details
def edit_student():

    # getting student details and converting to lower case
    student_id = input("\nEnter Student's ID: ")

    #  handling exception of value error
    try:
        student_id = int(student_id)
    except ValueError:
        print("Student ID must be an integer. Be careful next time.")
        edit_student()

    # fetching details based on mentioned id
    # sql query and values to fetch data from the database
    sql_query = "SELECT * FROM students where id = "+str(student_id)
    my_database.execute(sql_query)
    student = my_database.fetchall()

    # using pretty table library to show data
    pretty_table_object = PrettyTable()

    # table header
    pretty_table_object.field_names = ["Student ID", "Student's Name", "Subject"]

    # table body
    pretty_table_object.add_row([student[0][0], student[0][1], student[0][2]])

    # converting data to an string and print it on the screen
    student_table = pretty_table_object.get_string()
    print("\n"+student_table+"\n")

    # now taking updated input of student details from user
    # getting student details and converting to lower case
    student_name = input("\nUpdate Student's Name: ")
    subject = input("Update Student's Subject: ")
    s_name = s_subject = ""
    if not student_name.replace(' ','').isalpha() or  not subject.replace(' ','').isalpha():
        print("You are only allowed to use alphabetical characters. Be careful next time.")
        edit_student()
    else:
        s_name = student_name.title()
        s_subject = subject.upper()

    # sql query and values to insert data to the database
    sql_query = "UPDATE students SET name=%s, class=%s WHERE id=%s"
    values = (s_name, s_subject, student_id)

    # executing query to send data to the DB
    my_database.execute(sql_query, values)

    # to save changes this command is used (isse zada is k bare mai kuch nai pata :P)
    db_connection.commit()

    # success message
    print("\nBooyeah! You have successfully updated "+s_name+"'s details.")

    # asking user if he/she wants to edit more students or not
    desire = input("\nDo you want to edit more student (y/n)?: ")
    desire = desire.lower()

    # taking decision on the bases of users above input
    if desire == 'y':
        edit_student()
    else:
        sr_system()


# function to delete an specific student
def delete_student():

    # getting student details and converting to lower case
    student_id = input("\nEnter Student's ID: ")

    #  handling exception of value error
    try:
        student_id = int(student_id)
    except ValueError:
        print("Student ID must be an integer. Be careful next time.")
        edit_student()

    # fetching details based on mentioned id
    # sql query and values to fetch data from the database
    sql_query = "SELECT * FROM students where id="+str(student_id)
    my_database.execute(sql_query)
    student = my_database.fetchall()

    # using pretty table library to show data
    pretty_table_object = PrettyTable()

    # table header
    pretty_table_object.field_names = ["Student ID", "Student's Name", "Subject"]

    # table body
    pretty_table_object.add_row([student[0][0], student[0][1], student[0][2]])

    # converting data to an string and print it on the screen
    student_table = pretty_table_object.get_string()
    print("\n"+student_table+"\n")

    # asking user if he/she wants to edit more students or not
    permit_to_delete = input("\nAre your sure you want to delete " + student[0][1] + "'s details (y/n)?: ")
    permit_to_delete = permit_to_delete.lower()

    # taking decision on the bases of users above input
    if permit_to_delete == 'y':

        # SQL query to delete value from database and its execution
        sql_query = "DELETE FROM students where id="+str(student_id)
        my_database.execute(sql_query)
        db_connection.commit()

        # success message
        print("\nBooyeah! You have successfully deleted " + student[0][1] + "'s details.")

        # asking user if he/she wants to edit more students or not
        desire = input("\nDo you want to delete more student (y/n)?: ")
        desire = desire.lower()

        # taking decision on the bases of users above input
        if desire == 'y':
            delete_student()
        else:
            sr_system()
    else:
        sr_system()

# function to download the data from the database
def download():

    # sql query and values to fetch data from the database
    sql_query = "SELECT * FROM students"
    my_database.execute(sql_query)
    students = my_database.fetchall()

    # writing csv
    with open("student-details.csv", "w") as studentDetails:
        wr = csv.writer(studentDetails)
        wr.writerow(students)

    # writing json
    with open("student-details.json", "w") as studentDetails:
        json.dump(students, studentDetails)

    print("\n*** You have successfully downloaded the details of students. ***\n")
    # print(students_table)
