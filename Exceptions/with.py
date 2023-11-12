# Exceptions

filename = 'Users/flavio/test.txt'

# try:
#     file = open(filename , 'r')
#     content = file.read()
#     print(content)
# finally:
#     file.close()


with open(filename , 'r') as file:
    content = file.read()
    print(content)