dog = { "name": "Roger","age":8 ,
"color": "green"}

dog["name"] = "Syd"

print(dog['name'])

print(dog.get("name"))

print(dog.get("color","brown"))

print(dog.pop("name"))

print(dog)

print(dog.popitem())
print(dog)