import random

random_num=random.randint(1,10)
cont="y"
while(cont=="y"):
    x=int(input("guess a number betwn 1 and 10: "))
    if(x==random_num):
        print("u have guessed right, u won!!")
        cont=input("do u want to keep playing (y/n): ")
        random_num=random.randint(1,10)


    elif(x<random_num):
        print("u have guessed low ")    
    else:
        print("you have guessed high ")    

