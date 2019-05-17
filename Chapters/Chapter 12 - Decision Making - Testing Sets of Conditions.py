# what is we want to test multiple conditions in IF or ELIF tester?
# we use "and/or" operators to test multiple conditions in a single test
# 'and' is used when we want both conditions to be true
# 'or' is used when we want any one condition to be true


full_name = "Muhammad Azlaan"

if full_name == "Muhammad" + " " + "Azlaan" or full_name == "Muhammad" + " " + "Mahad": # any one condition to be true
    print("Welcome ", full_name)

elif full_name.isalpha() != True and full_name.isalpha() == False: # both conditions to be true
    print("Please use only letters in your name.")

else:
    print("Who are you ?")