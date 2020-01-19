n=input()
k={cha:n.count(cha)for cha in n}
print(k)
l=(sorted(k.items(),key=lambda kv:(kv[1],kv[0])))

for i in l:
    print(i,end='')
