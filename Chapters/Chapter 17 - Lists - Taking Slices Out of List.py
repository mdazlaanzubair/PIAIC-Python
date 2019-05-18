# If we want to break array into two we call it are slice

# All we need to do is just mention the start and end index from where we want to cut the list
# thats how it works
fruits = ["Apple", "Orange", "Mango", "Banana", "Cherry"]
fav_fruits = fruits[:3] #if we'll not mention starting index it takes 0 by default
print("My All Time Favorite Fruits: ", fav_fruits)

rare_fruits = fruits[4:] #if we'll not mention ending index it takes the ending index of the list by default
print("Fruits I Eat Rarely: ", rare_fruits)

all_fruits = fruits[1:4]
print("Fruits Almost Everyone Like: ", all_fruits)