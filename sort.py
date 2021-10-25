myList = ["schwarz", "Weiss", "grün", "Gelb", "lila", "braun", "beige", "Rot"]
# first uppercase then sorted lowercase
print(sorted(myList))

print(sorted(myList,key=str.lower))
