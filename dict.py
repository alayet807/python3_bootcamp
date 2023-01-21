#creating dictionary
d1={"name":"kho", "roll":16,"addr":"badda"}
d2=dict(name="kho",roll=16,addr="badda") #dict(key:'value)#key cannot be list,no duplicate key

#accessing
d1["name"]
for x in d1.values():
    print(x)
for y in d1.keys():
    print(y)    
for k,v in d1.items():#.items return all key value pair as tuple in a list
    print(k,v)    
#methods 
#clear() makes dic empty dic  
# {}.fromkeys([iterable kichu like list],value)   return a dic of keys from the list whose value set to value
#pop(key)
#d1.update(d2) d1 er sathe d2 add kore dei
#dic compre syn> {something:something for x in iterable}#by default key ke iterate kore.jodi key value duitakei iterate korte chai tobe .items use korbo

d3={"first":2,"second":4,"third":6}
new_d3={k:v**2 for k,v in d3.items()} ##{"first":4,"second":16,"third":36}
d4={x:x**2 for x in [2,4,6] } ##{2:4,4:16.6:36}
d5={x:"even" if x%2==0 else "odd" for x in [1,2,3,4]}
print(d5)