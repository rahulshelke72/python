dog = { "name": "Roger","age":8 ,"color": "green"}

dog["name"] = "Syd"

print(dog['name'])

print(dog.get("name"))

print(dog.get("color","brown"))

print(dog.pop("name"))

print(dog)

print(dog.popitem())
print(dog)

print(list(dog.keys()))
print(dog.values())

print(list(dog.items()))

