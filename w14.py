'''rows=int(input())
coef=1
for i in range (rows):
    for space in range(rows-i):
        print("  ",end='')
    for j in range(rows+1):
        if j==0 or i==0:
            coef=1
        else:
            coef=coef*(i-j+1)/j
	print(coef,end='')
    print()'''
	    
n=int(input())
c=1
for i in range(n):
    for k in range(n-i):
        print(" ",end='')
    for j in range(i+1):
        if j==0 or i==0:
            c=1
        else:
            c=c*(i-j+1)//j
        print(c,end=' ')
    print()
