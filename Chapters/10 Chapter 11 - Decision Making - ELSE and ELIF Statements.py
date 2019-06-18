# ELIF is similar like IF, we use it when we have to check multiple conditions.
# ELSE is used in exceptional cases when all conditions becomes false we ren the code
# of ELSE. Usually it's used to show errors to the users

full_name = "Muhammad Ali"
if full_name == "Muhammad" + " " + "Azlaan":
    print("Welcome ", full_name)
elif full_name == "Muhammad" + " " + "Mahad":
    print("Hi! ", full_name)
else:
    print("Who are you ?")