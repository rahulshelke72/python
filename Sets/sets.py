#Sets - contains Unique elements
set1 = {"Roger" , "Syd" ,"Roger"}
set2 = {"Roger"}

# Intersection
intersect = set1 & set2
print(intersect)

#Union
union = set1 | set2
print(union)

diff = set1 - set2
print(diff)

#Superset and Subset
mod = set1 > set2
print(mod)

mod2 = set1 < set2
print(mod2)

print(list(set2))
print("Roger" in  list(set1))

