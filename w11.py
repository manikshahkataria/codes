s=input()
l=[]
c=[]
for i in s:
    l.append(i)
print(l)
lh=len(l)
ran=lh//2
def opera(c):
    for j in range(1,len(c),2):
        
        
        if c[1]=='A':
            k=int(c[j-1])&int(c[j+1])
            return k
        elif c[1]=='B':
            k=int(c[j-1])|int(c[j+1])
            return k
        else:
        
            k=int(c[j-1])^ int(c[j+1])
            return k

for j in range(1,ran+1):
    
    c.append(l[0])
    c.append(l[1])
    c.append(l[2])
    
    an=opera(c)
    
    del l[:3]
    l.insert(0,an)
    
    del c[:]
    
print(l,'this is the answer')

