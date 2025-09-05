list1 = [("Pilani", "CS", 327), ("Pilani", "Chemical", 247), ("Pilani", "MSc. Eco", 271), ("Pilani", "MSc. Bio", 236),
    ("Goa", "CS", 301), ("Goa", "Chemical", 239), ("Goa", "MSc. Eco", 263), ("Goa", "MSc. Bio", 234),
    ("Hyderabad", "CS", 298), ("Hyderabad", "Chemical", 238), ("Hyderabad", "MSc. Eco", 261), ("Hyderabad", "MSc. Bio", 234)]

dict1 = {}
for camp, branch, mark in list1:
    if camp not in dict1:
        dict1[camp] = {}
    dict1[camp][branch] = mark

print(dict1)
