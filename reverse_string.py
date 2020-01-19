
def reverse(i):
    k=i[::-1]
    if (k==i):
        return True
    else:
        return False

fl=[]

n=input().split(' ')
for i in n:
    
    pali=reverse(i)
    if pali==True:
        fl.append(i)
    else:
        continue
if (fl!=[]):
    print(max(fl,key=len))
else:
    print(0)
