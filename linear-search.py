lis=[]
num=int(input('enter the size of list \t'))
for n in range(num):
    number=int(input('enter number in sorted order\t'))
    lis.append(number)
found=False
x=int(input('enter the no to be serched'))
for i in range(len(lis)):
    if x== lis[i]:
        found=True
        print('\n%d found at position %d'%(x,i))
        break
if not found:
    print('\n%d is not found'%x)
