def sel_sort(l):
    for i in range(len(l)-1):
        min_value=i
        for j in range(i,len(l)):
            if l[j]< l[min_value]:
                min_value= j
        temp= l[i]
        l[i]=l[min_value]
        l[min_value]=temp

l=[5,3,8,6,7,2]
sel_sort(l)
print(l)
