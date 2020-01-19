a=input()
i=0
for i in range(len(a)):
    j=i
    for j in range(len(a)):
        print(a[i:j+1],end=' ')
        j=j+1
    i=i+1
