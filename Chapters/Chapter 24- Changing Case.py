# changing case it is a necessary thing in programming cause we can't predict what input will
# come from the user end so we use change case methods like upper, lower, and title to convert
# the input to the desired or required pattern

# let's take a look of our previous program in this program if the user enters a place in all caps
# then only it matches the result like: (NEELUM VALLEY) but it could be (NEELUM VALLEY, Neelum Valley, neelum valley)
# also but the program will not understand only exactly matched inputs here comes the change case methods

# Clean Places to visit in Pakistan
# clean_places = ["NEELUM VALLEY", "SIRI PAYE", "LALAZAAR", "KAGHAAN VALLEY", "CHARNA ISLAND"]
# city_to_check = input("Enter A Place You Want To Visit In Pakistan: ")
# for place in clean_places:
#     if city_to_check == place:
#         print("It's the cleanest place of Pakistan: ", city_to_check)
#         break
#     elif city_to_check == "Pakistan" or city_to_check == "pakistan":
#         print(city_to_check, "is not a clean place according to our record")
#         break
#     else:
#         print(city_to_check, "is not a clean place according to our record")
#         break

# here is the same program but with the change case methods
# Clean Places to visit in Pakistan
clean_places = ["NEELUM VALLEY", "SIRI PAYE", "LALAZAAR", "KAGHAAN VALLEY", "CHARNA ISLAND"]
city_to_check = input("Enter A Place You Want To Visit In Pakistan: ")
city_to_check = city_to_check.upper() # here we convert user input to uppercase no matters what case was came from user
for place in clean_places:
    if city_to_check == place:
        print("It's the cleanest place of Pakistan: ", city_to_check)
        break
    elif city_to_check == "Pakistan" or city_to_check == "pakistan":
        print(city_to_check, "is not a clean place according to our record")
        break
    else:
        print(city_to_check, "is not a clean place according to our record")
        break

lower_case = input("Enter Your Name: ")
lower_case = lower_case.lower() # changing input to lower case
print("Your Name Converted to Lower-Case: ", lower_case)

upper_case = input("Enter Your Name: ")
upper_case = upper_case.upper() # changing input to upper case
print("Your Name Converted to Upper-Case: ", upper_case)

capitalized = input("Enter Your Name: ")
capitalized = capitalized.title() # changing input to capitalized form where first letter of each word will be capital
print("Your Name Converted to Capitalized Form: ", capitalized)