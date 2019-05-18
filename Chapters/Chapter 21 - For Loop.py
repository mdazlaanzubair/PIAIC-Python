# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# Clean Places to visit in Pakistan
clean_places = ["NEELUM VALLEY", "SIRI PAYE", "LALAZAAR", "KAGHAAN VALLEY", "CHARNA ISLAND"]
city_to_check = "NEELUM VALLEY"
for place in clean_places:
    if city_to_check == place:
        print("It's the cleanest place of Pakistan: ", city_to_check)
        break
    else:
        print(city_to_check, "is not a clean place according to our record")
        break
