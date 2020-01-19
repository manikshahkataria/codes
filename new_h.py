list1=[]
numb=int(input(""))

for i in range(numb):
    data=int(input())
    list1.append(data)
    
for i in range(0,numb):
    for j in range(0,numb-1):
        if list1[j]>list1[j+1]:
            swap=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=swap
            
print(list1[numb-2])
      
