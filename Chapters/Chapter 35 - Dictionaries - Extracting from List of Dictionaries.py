list_of_students = [
    {
        "id": 1,
        "fname": "Azlaan",
        "lname": "Zubair",
        "city": "Karachi",
    },
    {
        "id": 2,
        "fname": "Ali",
        "lname": "Ahmed",
        "city": "Islamabad"
    },
    {
        "id": 3,
        "fname": "Basit",
        "lname": "Ali",
        "city": "Lahore"
    },
]

print("\nExtracting a dictionary from the list:")
dictionary1 = list_of_students[0]
dictionary2 = list_of_students[1]
dictionary3 = list_of_students[2]

print("\n", dictionary1)
print("", dictionary2)
print("", dictionary3)

print("\nExtracting information out of dictionary from the list:")

print("\n Student's ID:", dictionary1["id"])
print(" Student's First Name:", dictionary1["fname"])
print(" Student's Last Name:", dictionary1["lname"])
print(" Student's City:", dictionary1["city"])