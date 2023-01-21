"""

"""
#pass by value#pass by ref
class Cat:
    def __init__(self,color,action):
        self.color=color 
        """ ekhane self object othoba instance ta bujhasse,jei object ei 
        constructor ke call korbe. self.color mane shei instance er variable. 
        self.jai likhbo shetai variable. tar moddhe receive hosse color er value. self.x=color likhle x variable,
        color hosse argument. self. na likhe shudhu variable likhle ta method er baire
        access kora jabe na """
        self.action=action
    def view(self,num,clr):
        num=num+5
        clr1=clr
        clr1[0]="green"
        print("inside method: ", num)  
        print("inside method: ", clr1)
colors=["black","red","blue"]
c1=Cat("white","jumping")
x=55
c1.view(x,colors) 
#colors list,tai tar ref pass hosse.eijonno method er moddhe change korleo orignaltai change hoi
print("method outside ",x)
print("method outside ", colors)
#print(c1.num) error karon num to instance er variable na. self.num nai tai        

##method overloading: 
"""class e same method er name but parameter alada.kintu python e directly 
method overload kora jai na. dispatch library import kore overload kora jai
tobe same uddessho serve hoi *args diye
""" 
from multipledispatch import dispatch
class calc:
    @dispatch(int,int)
    def product(self,a,b):
        print(a*b)
    @dispatch(int,int,int)
    def product(self,a,b,c):
        print(a*b*c)

    @dispatch(float,float)
    def product(self,a,b):
        print(a*b)     

    #@dispatch na dile last method ta shudhu kaj korbe   
    #constructor overloading
class Student:
    def __init__(self,*info):
        if len(info)==3:
            self.name=info[0]
            self.id=info[1]
            self.gpa=info[2]
        elif len(info)==2:
            self.name=info[0]
            self.id=info[1]    
        else:
            self.name=info[0]    

    #operator overloading
    # num1+num2 dile num1.__add__(num2) method call hoi auto. ekivabe duita string o eta
    # diye add kora jai.amra jodi duita object ke add korte jai tobe __add__ ei method ke 
    # amader class e implement kora lagbe

    class data:
        def __init__(self,x):
            self.x=x

        def __add__(self,other):
            return self.x+other.x

    num1=data(10)
    num2=data(20)
    str1=data("cse")
    str2=data("102")    
    print(num1+num2)# num1.__add__(num2)
    print(str1+str2)
    #out>30, cse102
    #encapsulation
    """private korar jonno variable/method er age __ dibo.
    self.__name=name
    def __method
    private method class er baire theke call kora jai na.kono public method er vitor korar jai
    """
    #class/static variable:  
    """jei variable object er upor depend kore na,same class er sob object er 
    jonno same thakbe
    class A: x class er niche lekha lgbe. method/constructor e thkbe na
    class variable update korte self.x na likhe A(class name).x
    """
    #class method: parameter hisabe cls r call korar somoy class name diye call
    class Employee:
        org_name="entropy"

        def __init__(self,name):
            self.name=name

        @classmethod
        def info(cls):
            print(cls.org_name)           


    #static method: eta self/cls kono parameter nei na,but other parameter nite pare
    #etake call korte class name likhle hbe
    #static r class method eki,class method use korbo jokhn sob object ei oi method kaje lagbe
    #static method just utility function er moto,extra kono kaje lagle
        
        @staticmethod
        def detail():
            print("this is static")

    Employee.info()
    Employee.detail()        

#inheritence
"""
child class parent er sob inherit korbe.but parent child er kichui inherit korbe na.
jodi parent duita thake tokhn left parent priority pabe.
parent r child e same naame method thakle tokhon child er method call hobe. etake
method override bole. duitakei call korte child er moddhe super call korte hbe.
class A:
class B(A):
"""
#has-a relation(composition)
"""
"""
class Engine:
    def __init__(self,cc):
        self.capacity=cc
    def start(self):
        print("engine started")
    def stop(self):
        print("engine stopped")

class Car:
    def __init__(self,name,cc):
        self.name=name
        self.engine=Engine(cc)                

    def run(self):
        print(self.engine)
        self.engine.start()
        print("car is running")
c1=Car("bmw",2000)
c1.run()

  

     #abstract

from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def taste(self):
        pass

class pizza(food):
    def size(self):
        print("hi")

    #jehetu eta food class ke inherit kore,tai er moddhe taste abstract method ashce
    # tai pizza o abstract class hoye gese.tai etar object create kora jabe na
    # tai abstract method ke override korte hbe
    def taste(self):
        print("tasty")     