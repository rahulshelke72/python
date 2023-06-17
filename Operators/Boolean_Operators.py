
condition1 = True
condition2 = False

not condition1  #False
condition1 and condition2   #False
condition1 or condition2   #True

print(0 or 1)  ## 1
print(False or 'hey')  ## 'hey
print('hi' or 'hey')  ## 'hi'
print([] or False)  ## 'False'

print(0 and 1)   ## 0
print(1 and 0)   ## 0
print(False  and 'hey')  ##False
print('hi' and 'hey')  ## 'hey'
print([] and False)  ## []
print(False and []) ##False



