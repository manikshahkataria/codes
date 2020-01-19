string=input("enter string")
length=len(string)
for row in range (length):
    for col in range(row,-1,-1):
        print(string[col],end="")
    print()    
