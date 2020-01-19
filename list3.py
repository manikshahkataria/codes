a=[]
n=input().split(" ")
for i in n:
    a.append(int(i))
print(a)
a.sort()
print(a[0])
print(a[-1])
'''print(a[0]+a[1])
#or 
keyboards = list(map(int, input().rstrip().split()))
print(keyboards)
'''
