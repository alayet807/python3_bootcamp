#creating list
l1=[1,2,36,7,4,9,0]
r=range(1,10)
l2=list(r)
#list function
#extend() or + new list add kore
#append() last e ekta element add kore
#pop() last element remove kore
#remove("element")
#insert(index,"element")
s=" is my friend ".join(["kho","mane"]) #dot er age ja thakbe ta duitar majhe thakbe seperator hisabe
#slicing
print(l1[2:1:-1]) #2 index theke ulta dike 1 index er ag porjonto jabe
#list comprehension
#syntax= [something(can be operation on that element or different) for element in list]
l3=[x*3 for x in l1]
#list compre with condition
l3=[x for x in l3 if x%2!=0] #jodi shudhu if thake
l3=[x if x%2==0 else x*2 for x in l1] #jodi else o thake
#nested list compre
l4= [[val for val in range(1,3)] for x in l1]
print(l4)
