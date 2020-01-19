string=input("enter string")
length=len(string)
for row in range (length):
    for col in range(0,row+1):
        print(string[row],end="")
        length=length+1
    print()    
