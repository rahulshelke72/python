
def change(value):
    value["name"] = "syd"

val = {"name":"beau"}
change(val)
print(val)


def hello(name):
    if not name:
        return
    print('Hello '+name + '!')

hello("Beau")


def hello2(name):
    print('Hello '+name + '!')
    return name , "Beau",8

print(hello2("Syd"))

