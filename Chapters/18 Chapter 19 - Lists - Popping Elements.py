# In previous chapter we use delete and remove method for deleting the elements from list
# But sometimes we use to delete element from the list but want to keep it so we use pop method for it

fruits = ["Apple", "Orange", "Mango", "Banana", "Cherry"]

# pop method is a method that accepts index and takes out that element from the list
fav_fruits = fruits.pop(2)
print("Fruit That Everyone Likes: ", fav_fruits)

# another example
cheap_fruits = fruits.pop(2)
print("Cheapest Fruit: ", cheap_fruits)