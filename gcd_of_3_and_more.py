def find_gcd(x,y):
    while(y):
        x,y=y,x%y
        print(x)
    return x
    

n=list(map(int,input().split( )))
num1=n[0]
num2=n[1]
gcd=find_gcd(num1,num2)
for i in range(2,len(n)):
    gcd=find_gcd(gcd,n[i])
print(gcd)
