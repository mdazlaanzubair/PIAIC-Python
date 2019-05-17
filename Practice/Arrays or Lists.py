# initializing cities of pakistan in an array
cities = ["Karachi", "Islamabad", "Lahore", "Gilgit", "Sialkot", "Hyderabad"]
separator = ", "

print("\nCities of Pakistan: ", separator.join(cities))

# extracting clean cities into another array
# slicing the array `array_name[start_index:end_index]` it breaks the array from the starting index to ending index
clean_cities = cities[:]
print("\nClean Cities of Pakistan: ", separator.join(clean_cities[1:4]))

# popping out city of cold regions from array
# 'array_name.pop(index_number)' take out that value from the array
cold_city = cities[:]
print("\nCold City of Pakistan: ", cold_city.pop(3))

# removing cities of sindh regions from array
# using `.remove()` function which accepts value of an element of array to remove it
punjab_cities = cities[:]
punjab_cities.remove('Karachi')
punjab_cities.remove('Hyderabad')
print("\nCities of Non-Sindh Region of Pakistan: ", separator.join(punjab_cities))

# deleting cities of non-sindh region from array
# using `del` method which accepts array index to remove an element
sindh_cities = cities[:]
del sindh_cities[1]
del sindh_cities[1]
del sindh_cities[1]
del sindh_cities[1]
print("\nCities of Sindh Region of Pakistan: ", separator.join(sindh_cities))

# adding element to the array
# using `array_name.append("item_value")` insert value in the end of the array
states = ["Sindh", "Punjab", "Balochistan", "KPK"]
states.append("FATA")
print("\nStates of Pakistan: ", states)

# using `array_name.extend(array2_name)` merge two arrays into one
rainbow_color_names = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]
rainbow_color_codes = ["#9400D3", "#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000"]
rainbow_color_names.extend(rainbow_color_codes)
print("\nRainbow Colours with their Codes Respectively: ", separator.join(rainbow_color_names))

# using `array_name.insert(index_number, "item_value")` insert value at the specified place in array
prime_numbers = ["2", "3", "7", "11", "13", "17", "19", "23", "29"]
prime_numbers.insert(2, "5")
print("\nList of all Prime Numbers: ", separator.join(prime_numbers))