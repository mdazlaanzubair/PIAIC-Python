dictionary = {
    "fname": "Basit",
    "lname": "Ali",
    "languages": ["Python", "Javascript", "PHP"]
}

info = """
        First Name: {} 
        Last Name: {}
        Programming Languages: {}
       """
info = info.format(dictionary["fname"], dictionary["lname"], dictionary["languages"])
print(info)