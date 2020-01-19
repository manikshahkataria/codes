

'''for i in range(4):
    for j in range(i):
        print(chr(97+j),end=" ")
    print()
for i in range(7,0,-1):
    k=0
    s=1
    l=0
    for j in range(i):
        
        print(chr(65+k),end='')
        k=k+1
    
    
        
    print()'''
n=int(input())
k=1
for i in range(0,n+1):
    for j in range(n-i+1):
        print(chr(65+j),end='')
    if (i!=0):
        print(' '*k,end='')
        k=k+2
    #for k in range(0,i*2-1):
     #   print(' ',end='')

    if (i==0):
        
        for l in range(n-i-1,-1,-1):
        
            print(chr(65+l),end='')
    else:
        for l in range(n-i,-1,-1):
            print(chr(65+l),end='')
    print()
    
