def rev(n):
    return n[::-1]
def pali(n):
    r=rev(n)
    n=str(int(r)+int(n))
    
    r=rev(n)
    if(n==r):
        return n
    else:
        pali(n)
    
        
    




n=input()
print(pali(n))
