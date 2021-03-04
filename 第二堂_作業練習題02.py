sum=0
m=int(input("請輸入迴圈次數:"))
for i in range(1,m):    
    if i%2==0:
       print(i)
       sum+=i
print("偶數加總=",sum)