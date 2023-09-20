# map() , filter() , reduce() 

numbers = [1,2,3]

# def double(a):
#     return a * 2

double = lambda a:a*2


# result = map(double,numbers)

result = map(lambda a:a*2,numbers)


print(list(result))