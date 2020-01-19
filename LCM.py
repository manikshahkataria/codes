a=int(input('enter 1st'))
b=int(input('enter 2nd'))
if a>b:
    i=a
else:
    i=b
while i<=a*b:
    if(i%a==0 and i%b==0):
        lcm=i
        break
    i=i+1
print(lcm)

    
    
