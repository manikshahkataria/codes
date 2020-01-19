l=[]
n=int(input('enter the no of walls'))
print('enter height of walls')
for i in range(n):
      x=int(input(''))
      l.append(x)
print(l)      
j=int(input('enter the  length of jump'))
y=int(input('enter the length he slip back'))

def jumpcount(j,y,n,l):
    jumps=0
    for i in range(n):
        if (l[i]<=j):
            jumps+=1
            continue
        h=l[i]
        while(h>j):
            jumps+=1
            h=h-(j-y)

        jumps+=1
    return jumps

print( jumpcount(j,y,n,l))
