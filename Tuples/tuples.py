#Tuples 
# Tuples immutable objects
# Once created cannot change it


names = ("Roger","Syd","Beau")

print(names[0])
print(names.index("Roger"))

print("Roger" in names)

print(names[0:2])

print(sorted(names))

#it will generate error tuples cannot chnaged
newTuple = names + ("Tina","Quincy")