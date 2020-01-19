

def multi(ls1):
    f=[]
    
    for i in range(len(ls1)):
        l=1
        r=1
        for k in(ls1[:i]):
            l=k*l
        for m in(ls1[i+1:]):
            r=m*r
        f.append(l*r)
            
            
    return f
        
        #for j in (ls1[i+1:]):
         #   print(j)
        #for k in (ls1[:i]):
         #   print(k)
        
n=list(map(int,input().rstrip().split()))
print(multi(n))
