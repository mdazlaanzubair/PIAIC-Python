name_of_students = {
    1: "Ali Ahmed",
    2: "Raza Shaheen",
    3: "Shehzad Sheikh",
    4: "Azlaan Zubair",
    5: "Basit Ali"
}

# looping through keys of the dictionary
print("\nLooping through the keys of dictionary:")
for student_id in name_of_students.keys():
    print(student_id)

print("\nLooping through the values of dictionary:")
for name_of_student in name_of_students.values():
    print(name_of_student)

print("\nLooping through the key value pairs of dictionary:")
for item in name_of_students.items():
    print(item, "\n => Student's ID:", item[0], "Student's Name:", item[1], "\n")
