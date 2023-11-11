# Exceptions

try:
   raise Exception('An error!')
except Exception as error:
   print("inside")
   print(error)

class DogNotFoundException(Exception):
   pass

try:
   raise DogNotFoundException()
except DogNotFoundException:
   print('Dog not found!')