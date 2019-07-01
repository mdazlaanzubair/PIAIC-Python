from db_connection import *
from crud import *
import bcrypt



# authentication function to protect CRUD application
def authenticate_user():

    # a variable to limit the number of wrong tries to login the system
    login_attempt = 0

    while login_attempt < 3:

        # getting email from user
        username = input("Enter your email: ")

        # searching email in the database
        sql_query = "SELECT * FROM users where email=%s"
        value = (username,) # include comma',' to make the value variable tuple
        my_database.execute(sql_query,value)
        user = my_database.fetchall()

        if len(user) != 0:
            user_detail['name'] = user[0][1]
            user_detail['email'] = user[0][2]
            user_detail['password'] = user[0][3]

            # getting email from user
            password = input("Enter your password: ").encode() # password input by user
            db_passowrd = user_detail['password'].encode() # password from database

            # authenticate if credentials are right or wrong
            if bcrypt.checkpw(password, db_passowrd) and user_detail['email'] == username:

                # exiting loop
                login_attempt = 5
            else:
                print("Wrong username or password")
        else:
            print("Credentials doesn't match one of our records.")

        login_attempt += 1

    if login_attempt == 3:
        print("Your limit to attempt login exceeded. Try it Later")
    else:
        sr_system()


# register new user
def register_user():
    user_email = input("Enter User Email : ")

    # searching email in the database
    sql_query = "SELECT * FROM users where email=%s"
    value = (user_email,)  # include comma',' to make the value variable tuple
    my_database.execute(sql_query, value)
    user = my_database.fetchall()

    if len(user) != 0:
        print("\nThis user is already registered.")

        # getting email from user
        desire = input("Do you want to login? (y/n): \n").lower()

        # authenticate if credentials are right or wrong
        if desire == 'y':
            authenticate_user()
        else:
            register_user()
    else:
        user_name = input("Enter User Name : ").title()
        user_password = ''

        # creating loop to confirm password
        i = -1
        while i < 0:
            user_password = input("Enter User Password: ").encode()
            user_confirm_password = input("Confirm Password: ").encode()

            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(user_password, salt)
            hashed_confirm_password = bcrypt.hashpw(user_confirm_password, salt)

            if user_password == user_confirm_password and bcrypt.checkpw(user_password, hashed_confirm_password):
                user_password = hashed_password
                i = 1
            else:
                print("Password Confirmation failed. Try again.\n")
                i = -1 # run this loop again

        # adding this new user to the database
        # sql query and values to insert data to the database
        sql_query = "INSERT INTO users (name, email, password) values (%s, %s, %s)"
        values_to_db = (user_name, user_email, user_password)

        # executing query to send data to the DB
        my_database.execute(sql_query, values_to_db)

        # to save changes this command is used (isse zada is k bare mai kuch nai pata :P)
        db_connection.commit()

        # asking user if he/she wants to add more user or not
        desire = input("\nDo you want to add more users (y/n)?: ").lower()

        # taking decision on the bases of users above input
        if desire == 'y':
            register_user()
        else:
            sr_system()


# logout user function to end session
def logout():
    user_detail = {
        'name': '',
        'email': '',
        'password': ''
    }
    print("\n\n*** Your are Successfully Logged Out ***\n\n")
