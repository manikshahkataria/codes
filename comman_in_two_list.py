l=[2,3,5,'fhh']
k=[3,4,6,5,'fhh']
j=list(set(l).intersection(k))

print(j)
p=[i for i in l if i in k]# for comman elements
print(p)
#for different elements
d=[i for i in l + k if i not in k or i not in l]
print(d)


def Diff(l,k): 
    li_dif = [i for i in l + k if i not in l or i not in k] 
    return li_dif 
  
# Driver Code 
 
li3 = Diff(l,k) 
print(li3) 



print(l+k)
