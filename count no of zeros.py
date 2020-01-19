count=0
n=int(input("enter no"))
for i in range(n):
    s=str(i)
    
    for j in s:
        
        if(j=='0'):
            count=count+1
            print(s," ",count)
print("no of zeros",count)
