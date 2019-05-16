num1 = input("\nEnter A Number: ")
num2 = input("Enter Another Number: ")
val1 = 0
val2 = 0
message = "Initial Message"
error = "No Error"
try:
    # converting input from string to integer
    num1 = int(num1)
    num2 = int(num2)

    # checking input number one type
    if num1 >= 0 and num1%2 == 0: # if input is positive integer and even
        val1 = 1
    elif num1 < 0 and num1%2 == 0: # if input is negative integer and even
        val1 = 2
    elif num1 < 0 and num1%2 != 0: # if input is negative integer and odd
        val1 = 3
    elif num1 >= 0 and num1%2 != 0: # if input is positive integer and odd
        val1 = 4
    else:
        val1 = 0

    # checking input number two type
    if num2 >= 0 and num2%2 == 0: # if input is positive integer and even
        val2 = 1
    elif num2 < 0 and num2%2 == 0: # if input is negative integer and even
        val2 = 2
    elif num1 < 0 and num2%2 != 0: # if input is negative integer and odd
        val2 = 3
    elif num2 >= 0 and num2%2 != 0: # if input is positive integer and odd
        val2 = 4
    else:
        val2 = 0

    # setting information message for a user
    if val1 == 1 and val2 == 1:
        message = "Your both inputs are positive and even integers, "
    elif val1 == 3 and val2 == 3:
        message = "Your both inputs are negative and odd integers, "
    elif val1 == 1 and val2 == 2:
        message = "Your both inputs are even but first one is positive and second one is negative integer, "
    elif val1 == 2 and val2 == 1:
        message = "Your both inputs are even but first one is negative and second one is positive integer, "
    elif val1 == 1 and val2 == 4:
        message = "Your both inputs are positive but first one is even and second one is odd, "
    elif val1 == 4 and val2 == 1:
        message = "Your both inputs are positive but first one is odd and second one is even, "


    if val1 == 0 or val2 == 0: # error on wrong input
        print("\n Something went wrong please re run the program. Make sure you enter correct integers.")
    else:
        print("\n" + message + "Input Number One: " + str(num1) + ", Input Number Two: " + str(num2))
        print("\nSome Basic Operation On Your Input\n")
        print("Addition: " + str(num1 + num2))
        print("Subtraction: " + str(num1 - num2))
        print("Multiplication: " + str(num1 * num2))
        if num1 > num2:
            div = num1/num2
            print("Division: " + str(round(div, 2)))
        else:
            div = num2/num1
            print("Division: " + str(round(div, 2)))
        print("Average: " + str(round(((num1 + num2)/2), 2)))


except ValueError:
    print("\nPlease enter a valid number strings are not allowed!!!")