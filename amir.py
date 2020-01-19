'''n=list(map(int,input().split()))
l=n.copy()
c=[]
le=len(n)
def find(c):
    f=min(c)
    c.remove(f)
    ma=max(c)
    c.remove(ma)
    for i in c:
        k=i
    return k
for i in range(2,len(l),3):
    c.append(l[i])
    c.append(l[i-1])
    c.append(l[i-2])    
    v=find(c)'''
test_list = [1, 3, 4, 6, 7,7] 
  
# printing original list  
print ("The original list is : " + str(test_list)) 
  
flag = 0
  
# using set() + len() 
# to check all unique list elements 
flag = len(set(test_list)) == len(test_list) 
  
  
# printing result 
if(flag) : 
    print ("List contains all unique elements") 
else :  
    print ("List contains does not contains all unique elements") 
    
print(set(test_list))
