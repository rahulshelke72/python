#Nested Functions 

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)


talk('I am going to guy the milk')


def count():
    count = 0 
    
    def increment():
        nonlocal count = count + 1
        print(count)
    
    increment()