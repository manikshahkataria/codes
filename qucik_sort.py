def quick(l):
    length=len(l)
    if length<=1:
        return l
    else:
        pivot=l.pop()
        
    item_greater=[]
    item_smaller=[]
    for item in l:
        if item > pivot:
            item_greater.append(item)
        else:
            item_smaller.append(item)
    return quick(item_smaller) + [pivot] + quick(item_greater)
l=[0,9,3,8,2,7,5]
print(quick(l))
