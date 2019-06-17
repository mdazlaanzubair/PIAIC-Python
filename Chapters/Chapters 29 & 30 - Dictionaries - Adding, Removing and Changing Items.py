# =================================
# adding element to the dictionary
# =================================

name_of_students = {
    1: "Ali Ahmed",
    2: "Raza Shaheen",
    3: "Shehzad Sheikh"
}
name_of_students[4] = "Azlaan Zubair"
print("\nList of Students after adding one in it:\n", name_of_students)

# ===================================
# changing element in the dictionary
# ===================================

print("\nList of Students before changings\n", name_of_students)
name_of_students[4] = "Muhammad Azlaan Zubair"
print("\nList of Students after changings\n", name_of_students)


# ===================================
# removing element in the dictionary
# ===================================

print("\nList of Students before removing elements\n", name_of_students)
del name_of_students[4]
del name_of_students[1]
print("\nList of Students after removing elements\n", name_of_students)