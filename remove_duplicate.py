n=int(input("size"))
l=[]
fl=[]
for i in range(n):
    l.append(int(input("enter element")))
print("input array",l)
for num in l:
    if num not in fl:
        fl.append(num)
print("Distint elements are",fl)
