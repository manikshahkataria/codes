lower= int(input('enter lower limit'))
uper=int(input('enter the uper limit'))
for num in range(lower,uper+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
