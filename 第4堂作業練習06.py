import random 
count=0
ans=random.randint(1,100)
guess=0
minn=1
maxx=100
while ans!=guess:
    guess=int(input("請輸入0到100之間的整數:"))
    if ans>guess:
        print(guess+1,"~",maxx)
    if ans<guess:
        print(guess-1,"~",minn)
    count+=1          

print("猜對了，共猜:",count,"次")

