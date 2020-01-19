#sc=[17,45,41,60,17,41,76,43,51,40,89,92,34,6,64,7,37,81,32,50]
sc=[100,45,41,60,17,41,45,43,100,40,89,92,34,6,64,7,37,81,32,50]
lo=sc[0]
h=[]
l=[]
for i in sc:
    if (i>sc[0]):
        h.append(i)
        sc[0]=i
for i in sc:
    if (lo> i):
        l.append(i)
        lo=i

        
print(h)
print(l)
fl=[]
for num in l:
    if num not in fl:
        fl.append(num)
print(fl)
m=len(h)
g=len(fl)
print(m,g)
