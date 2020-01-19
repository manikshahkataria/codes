def bubsort(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp








l=[5,3,8,6,7,2]
bubsort(l)
print(l)
