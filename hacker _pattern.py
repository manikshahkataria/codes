'''d=int(input())
s=int(input())
st=(s-3)//2

ft=(d-1)//2
for i in range(ft+1,0,-1):
    for j in range(0,3*i-3):
        print("-",end="")
    print()
print("-"*d+'WELCOME'+"-"*d)
'''
N, M = map(int, input().split())
for i in range(1, N, 2):
    print (str('.|.' * i).center(M, '-'))
print ('WELCOME'.center(M, '-'))
for i in range(N-2, -1, -2):
    print (str('.|.' * i).center(M, '-'))
