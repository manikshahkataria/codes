n=int(input('enter the no'))
result=0
l=len(str(n))
while(n!=0):
    digit=n%10
    result=result+digit
    n=n//10

c=0
k=0
i=0
#for i in range(1,result+1):
while(i<=result):
    
    k=(result*i)
    
    i=i+1
    if k==n:
        c=c+1
        break
    else:
        c=c
        
    
    
if c>0:
    print('harshed no')
else:
    print('not harsherd no ')

