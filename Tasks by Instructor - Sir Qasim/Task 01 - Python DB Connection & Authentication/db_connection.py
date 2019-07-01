#  importing python mysql module to make connectivity between python program and mysql database
import mysql.connector

# performing check that if database connected or not
try:

    #  storing database information to which we want to connect this program
    db_connection = mysql.connector.connect(
        host="localhost",   # database host_name usually its localhost or 127.0.0.1
        user="root",        # username of database by default it's root or change it if you have another one
        passwd="",          # password of database by default it's none or put your database password if you have one
        database="piaic"    # name of the database you've created
    )

    #  executing python database connection command
    my_database = db_connection.cursor()

    # if database connected print it
    print("\nDatabase successfully Connected.\n")

# if database connection fails due to any cause runt the following block
except Exception as e:

    # if had an error connecting to the database
    print("\nDatabase Connection Error:\n\n", e)
