# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
b=[]
for i in range(0,a):
    a=input().split()
    if(a[0]=='insert'):
        b.insert(int(a[1]),int(a[2]))
        print(b)
    elif(a[0]=='remove'):
        b.remove(int(a[1]))
    elif(a[0]=='pop'):
        b.pop()
    elif(a[0]=='print'):
        print(b)
    elif(a[0]=='reverse'):
        b.reverse()
    elif(a[0]=='append'):
        b.append(int(a[1]))
        
    elif(a[0]=='sort'):
        b.sort()
        
