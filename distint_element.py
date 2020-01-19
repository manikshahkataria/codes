a=[10,20,30]
b= [20,25,30,40,50]
l=list(set(a) - set(b))
p=list (set(b)-set(a))
print(set(l+p))


p='maik'
p=set(p)
j='shah'
j=set(j)
k=list(p-j)
print(k)
f=list(j-p)
gg=f+k
print(gg)
