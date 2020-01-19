n=int(input('enter the no of students'))
a={}
for i in range(n):
    
    name=input('enter name')
    b=[]
    avg=[]
    for j in range(3):
        b.append(float(input('enter marks')))
        a[name]=b
    total=sum(b)
    avg.append(float((total)/3))
    a[name]=avg
print(a)
name=input('name u want to search')
for l in (a[name]):
    print(l,end='')
          
            
