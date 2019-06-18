# in previous lessons we are using fix values set in the varible but what if we want user to input something?
# to take user input in python we use input() method
# you must provide a variable to hold the user's input. If you omit
# it python breaks and shows error.


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

# one more thing, that python treats the value typed by the user as a string, even if it's a number
# so we need to convert it first before calculating it
user_input = input("Enter Your Monthly Income: ")
income = int(user_input)
tax = 0

if income < 50000:
    tax = 0
elif income > 50000 and income < 100000:
    tax = 10
elif income > 100000:
    tax = 20
else:
    print("Please make sure your input is positive integer!!!")

income_tax = (tax*income)/100

print("Your Monthly Income is: ", income)
print("Your Annual Income is: ", income*12)
print("Tax Applied: ", tax, "%")
print("Your Monthly Tax is: ", income_tax)
print("Your Annual Tax is: ", income_tax*12)