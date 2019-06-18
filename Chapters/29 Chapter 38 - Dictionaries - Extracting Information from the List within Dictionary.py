dictionary = {
    "fname": "Basit",
    "lname": "Ali",
    "languages": ["HTML", "CSS", "PHP", "JS"]
}

info = """
        First Name: {} 
        Last Name: {}
        Language: {}
       """
if "HTML" in dictionary["languages"] and "CSS" in dictionary["languages"] and "PHP" in dictionary["languages"] and "JS" in dictionary["languages"]:
    languages = ",".join(dictionary["languages"] )
else:
    languages = "Not a programmer"

info = info.format(dictionary["fname"], dictionary["lname"], languages)
print(info)