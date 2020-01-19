n=9

nha=n//2+1
for i in range(nha,0,-1):
    val=i-1
    for k in range(nha-i):
        print(" ",end='')
    for j in range(1,i*2):
        
        if(j<=i):
            val=val+1
            print(val,end='')
            
        else:
            val=val-1
            print(val,end='')
        
    print()
for i in range(2,nha+1):
    val=i-1
    for k in range(i,nha):
        print(" ",end='')
    for j in range(i*2-1):
        if (j<i):
            val=val+1
            print(val,end='')
           
        else:
            val=val-1
            print(val,end='')
    print()
        
