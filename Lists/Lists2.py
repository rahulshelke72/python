items = ["Roger", "Syd","beau" , "Quincy"]

items[1:1] = ["Test1"]

itemscopy = items[:]
items.sort(key=str.lower)
print(items)
print(itemscopy)

print(sorted(items,key=str.lower))



