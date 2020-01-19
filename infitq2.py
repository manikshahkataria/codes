n=input()
l=[]
f=[]
for i in n:
    l.append(i)
if(l[0]=='-'):
    f.append(l[0])
    for i in l:
        if(i.isnumeric()):
            f.append(i)
        else:
            continue
else:
    for i in l:
        if(i.isnumeric()):
            f.append(i)
        else:
            continue
s=''
s=s.join(f)
print(s)
    
