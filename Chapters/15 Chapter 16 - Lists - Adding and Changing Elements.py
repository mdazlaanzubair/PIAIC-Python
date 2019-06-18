# What if we want to add new item in a already created list?
# There are two methods of it one called append and second one is insert

# Adding item to a list using append method
fruits = ["Apple", "Orange", "Mango", "Banana", "Cherry"]
fruits.append("Grapes")
print("Fruits: ", fruits)
# here the new item is set at the end of the list
# this is what append do

# Adding item to a list using insert method
fav_fruits = ["Apple", "Orange", "Mango", "Banana", "Cherry"]
fav_fruits.insert(2, "Grapes")
print("Fruits: ", fav_fruits)
# here the new item is set on the mentioned index position of the array
# this is what insert do
# insert accept two parameter one is index of the array where you want
# to add item and second one for value
