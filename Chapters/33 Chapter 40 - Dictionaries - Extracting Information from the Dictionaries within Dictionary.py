list_of_users = {
    "user_1" : {
        "id" : 1,
        "fname" : "Ali",
        "lname" : "Ahmed",
        "email": "aliahmed@email.com"
    },
    "user_2" : {
        "id" : 2,
        "fname" : "Azlaan",
        "lname" : "Zubair",
        "email": "azlaanzubair@email.com"
    },
    "user_3" : {
        "id" : 3,
        "fname" : "Basit",
        "lname" : "Ali",
        "email": "basitali@email.com"
    }
}

# extracting information of a user1
user1 = """
            Username: {}{}
            Display Name: {} {}
            Email Address: {}
        """
user1 = user1.format(list_of_users["user_1"]["fname"], list_of_users["user_1"]["id"], list_of_users["user_1"]["fname"], list_of_users["user_1"]["lname"], list_of_users["user_1"]["email"])

# extracting information of a user2
user2 = """
            Username: {}{}
            Display Name: {} {}
            Email Address: {}
        """
user2 = user2.format(list_of_users["user_2"]["fname"], list_of_users["user_2"]["id"], list_of_users["user_2"]["fname"], list_of_users["user_2"]["lname"], list_of_users["user_2"]["email"])

# extracting information of a user3
user3 = """
            Username: {}{}
            Display Name: {} {}
            Email Address: {}
        """
user3 = user3.format(list_of_users["user_3"]["fname"], list_of_users["user_3"]["id"], list_of_users["user_3"]["fname"], list_of_users["user_3"]["lname"], list_of_users["user_3"]["email"])

# printing extracted information
print(user1)
print(user2)
print(user3)