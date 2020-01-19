num=1
n=int(input("enter rows"))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num,end=" ")
        num=num+1
    print()    
