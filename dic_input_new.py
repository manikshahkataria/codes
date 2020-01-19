k=int(input('how many inputs u want in dic'))
print('wirte key and value seprated by space')
f={ }
for i in range(k):
    n=input().split(' ')
    f.update({n[0]:n[1:]})
print(f)
for g,v in f.items():
    print(f"{g}:{v}")
