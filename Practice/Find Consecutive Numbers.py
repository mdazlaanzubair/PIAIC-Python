# original array to test
test_list = [1, 2, 3, 5, 6, 8, 10]

# array to show final result
result = []

# temporary value holders
start = ''
end = ''

# number of elements in list
elements = len(test_list)

# number of loops to iterate
loop_limit = len(test_list)-1

# setting last value of array to the variable
test_list_end = test_list[-1]

# for loop to start iterating in the test_array
for i in range(loop_limit):

    # setting first value of array in both value holders
    start = test_list[i]
    end = start

    # while loop to start converting consecutive numbers to range
    while test_list[i+1]-test_list[i] == 1 or test_list[i+1]-test_list[i] == -1:

        # setting second value to the end value holder
        end = test_list[i+1]

        # incrementing 'i' for while loop
        i += 1

    # checking if previously set value to the start holder is equal to end holder or not
    if start == end:

        # if condition true add it to the final result
        result.append(start)
    else:

        # if upper condition is false than concatenate both and add to the final result
        concat = str(start) + '-' + str(end)
        result.append(concat)

# adding the last value of array which was stored initially from test_array
result.append(test_list_end)


# print everything out
print("Original List:", test_list)
print("Elements in List:", elements)
print("Loop Limit:", loop_limit)
print("\nRange:", result)