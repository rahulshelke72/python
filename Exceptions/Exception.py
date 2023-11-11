# Exceptions

try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')
finally:
    result = 1
# try:
#     #
# except  :
#     # handler
# except  :
#     #handler
# else:
#     # no exceptions were raised , the code run successfully
# finally:
#     # do something in any case