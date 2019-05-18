# If we want to delete elements from array we use two methods for it
# one takes index to delete an element and one takes value to delete an element

fruits = ["Apple", "Orange", "Mango", "Banana", "Cherry"]

# del method is a method that accepts index and delete the value of that index from the list
# if we'll not mention starting index it takes 0 by default
fav_fruits = fruits[:3]
del fav_fruits[1]
print("My All Time Favorite Fruits: ", fav_fruits)

# remove method is a method that accepts value of element to delete it from the list
# if we'll not mention ending index it takes the ending index of the list by default
rare_fruits = fruits[3:]
rare_fruits.remove("Banana")
print("Fruits I Eat Rarely: ", rare_fruits)