list1=[]
numb=int(input("enter the size of list"))
print("enter elements")
for i in range(numb):
    data=(input())
    list1.append(data)
print(list1)    
for i in range(0,numb):
    for j in range(0,numb-1):
        if list1[j]>list1[j+1]:
            swap=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=swap
print(list1)            
