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

new_dictionary = {
    "id": 4,
    "fname": "Basit",
    "lname": "Ali",
    "city": "Lahore"
}
# adding a new dictionary to the list
list_of_students.append(new_dictionary)

print("\nExtracting a dictionary from the list:")
dictionary = list_of_students[3]
print("", dictionary)

print("\nExtracting information out of dictionary from the list:")
print("\n Student's ID:", dictionary["id"])
print(" Student's First Name:", dictionary["fname"])
print(" Student's Last Name:", dictionary["lname"])
print(" Student's City:", dictionary["city"])
print()