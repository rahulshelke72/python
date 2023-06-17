
done  = True

print(type(done) == bool)

if done:
    print("Yes")
else:
    print("No")

done1 = ""   #string empty it false in boolean
if done1:
    print("Yes")
else:
    print("no")

book_1_read = True
book_2_read = False
read_any_book = any([book_1_read,book_2_read])
print(read_any_book)

ingredients_purchased = True
meal_cooked = False
ready_to_serve = all([ingredients_purchased,meal_cooked])
print(ready_to_serve)