# As we used operators like (and/or) in previous lesson we can perform multiple conditions checks
# but that practice is good for two or three conditions, using more that three condition will make
# the code dirty and un-readable

var = 66
if var < 200:
    print("Expression value is less than 200")
    if var == 150:
        print("Which is: ", var)
    elif var == 100:
        print("Which is: ", var)
    elif var == 50:
        print("Which is: ", var)
    elif var < 50:
        print("Expression value is less than 50")
    else:
        print("Which is: ", var)
else:
    print("Expression value is greater than 200")
print("Good bye!")