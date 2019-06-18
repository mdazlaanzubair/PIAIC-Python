# nesting for loops in to each other

first_names = ["BlueRay ", "Upchuck ", "Lojack ", "Gizmo ", "Do-Rag "]
last_names = ["Zzz", "Burp", "Dogbone", "Droop"]

for fname in first_names:
    for lname in last_names:
        print(fname, lname)