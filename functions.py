#keyword argument

def exp(base,pow):
    return base**pow


exp(2,3) #8
exp(3,2) #9
exp(base=2,pow=3) #8
exp(pow=3,base=2) #8

#global

total=0
def incr():
    total+=1
    return total
#increment() will throw error because total is not defined in func scope,total was global thats
# outside of func. to correct this we have to specify global keyword in func scope
# def incr(): global total total+=1 return total

#nonlocal

def outer():
    count=0
    def inner():
        nonlocal count #count outer func er moddhe,func er baire na,tai eta global na. abar inner er jonno local o na.
        count+=1
        return count
    return inner()    


#*args
#jokhon kotogula argument pathabo eta fixed na. args tuple hisabe accept kore

def sum(*args):
    total=0
    for i in args:
        total+=i
    return total
sum(1,2,3)#6
print(sum(4,6)) 

#**kwargs (kwargs na hoye onno naam o hote pare)
#dictionary hisabe accept kore
def fv_col(**kwargs):
    for per,col in kwargs.items():
        print(f"{per} fav color is {col}")

fv_col(kho="red",mane="blue")    

##parameter ordering: parametrs,*args,default, **kwargs
def display (a,b, *args, inst="kho", **kwargs):
    return [a,b,args,inst,kwargs]
display(1,2,3,lastname="mane", job="inst") # a=1,b=2,args=(3,), inst="kho", kwargs={"lastname":"mane", "job":"inst"}

##unpacking tuple/list/dict
'''
*args e argument pathanor somoy sob element ke individually pathate hoi.
jemom:
def sum(*args):....
sum(1,2,3,4)
kintu jodi sum(any list/tuple) evabe pass kortam tahole error hoito. tokhon args er moddhe ([1,2,3,4],)
erokom tuple pass hoito. eijonno list/tuple pass korar somoy unpack korte hoi.
ta korar jonno argument jeta pass korbo tar age * dibo.
sum(*list)
r jodi function call e dict pass kori tokhn unpack korte ** dibo
'''