a=[]
n=int(input('enter the no of elements'))
for i in range(1,n+1):
    b=int(input('enter the elements'))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print('the even ',even)
print('the odd',odd)
print('sum of even',sum(even))
print('sum of odd',sum(odd))
