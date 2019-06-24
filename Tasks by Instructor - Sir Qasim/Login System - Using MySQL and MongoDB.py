from prettytable import PrettyTable
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="piaic"
)
my_database = db_connection.cursor()


# CRUD function of student registration system
def sr_system():

    # sasti c styling nothing else
    print("=================================")
    print("== STUDENT REGISTRATION SYSTEM ==")
    print("=================================")
    print("\nDirections:\n")
    print("1. Type 'a' to Add New Student")
    print("2. Type 'b' to View List of Students")
    print("3. Type 'c' and 'Student ID' to Edit Student Details")
    print("4. Type 'd' and 'Student ID' to Delete Student")

    # grabbing user's choice
    choice = input("\nEnter your command to proceed:")
    choice = choice.lower()

    # some sort of deciesion making on user's input
    if choice == 'a':
        # calling add new student function
        add_student()

    elif choice == 'b':
        # calling view list of students function
        view_students()

    elif choice == 'c':
        # calling edit student's details function
        def edit_student()

    elif choice == 'd':
        # calling delete student function
        print("calling Delete Function")

    else:
        # calling same function while showing a custom error
        print("Please use commands mentioned above only [a, b, c, d]")
        sr_system()


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
        desire = input("\nDo you want to add more student (y/n)?: ")
        desire = desire.lower()

        # taking deceision on the bases of users above input
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

    studets_table = pretty_table_object.get_string()
    print("\n"+studets_table)

    # asking user if he/she wants to go back to main function
    desire = input("\nDo you want jump back (y/n)?: ")
    desire = desire.lower()

    # taking deceision on the bases of users above input
    if desire == 'y':
        sr_system()
    else:
        view_students()



# edit student details
def edit_student():

    # getting student details and converting to lower case
    student_id = input("\nEnter Student's ID: ")

    # testing input type
    if type(student_id) is int or type(student_id) is float:
        student_id = int(student_id)
    else:
        print("Student ID must be an integer. Be careful next time.")
        edit_student()

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

        # asking user if he/she wants to edit more students or not
        desire = input("\nDo you want to add more student (y/n)?: ")
        desire = desire.lower()

        # taking deceision on the bases of users above input
        if desire == 'y':
            i += 1
        else:
            i = -1

    # if loop ends we'll get back to the main function again
    sr_system()

sr_system()
