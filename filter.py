"""
map er motoi.eta kono true false filtering kore.true hoile return kore
"""

num=[1,2,4,5,6]

even=list(filter(lambda x: x%2==0, num))#[2,4,6]
#combining map with filter
"""
names=["kho","man","al"]
return a new list with the string "your instructor is "+each value in the list,
but only if the value is less than 5 characters
"""
names=["kho","man","al"]
res=list(map(lambda x: "your instructor is "+x, filter(lambda y: len(y)<5, names)))
print(res)
