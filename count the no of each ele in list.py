arr=[1,2,3,4,5,4,3,2,1,3,4]
'''co={c:l.count(c) for c in l}
print(co)
print(max(co,key=co.get))
'''
'''def mid(l):
    
    bird_freq = [0, 0, 0, 0, 0, 0]
    for i in range(len(arr)):
        bird_freq[arr[i]] += 1
        print(bird_freq)
    return bird_freq.index(max(bird_freq))
print(mid(arr))'''

p=[]
for i in range(1,6):
    c=arr.count(i)
    p.append(c)
k=(p.index(max(p)))
print(k+1)




l=[10,20,20,10,10,30,50,10,20]
fi={d:l.count(d) for d in l}
print(fi)
p=list(fi.values())
print(p)
pair=0
for i in p:
    if (i%2==0):
        g=i//2
        pair=g+pair
    else:
        g=i//2
        pair=g+pair
print(pair)
    
