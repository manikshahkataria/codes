'''def palidrom(n):
    num=n
    d=0
    rev=0
    while n>0:
        d=n%10
        n=int(n/10)
        rev=rev*10+d
    if(num==rev):
        return True
    else:
        return False

x=int(input('enter the no'))
if palidrom(x):
    print(x,'palidrom')
else:
    print(x,'not palidrom')
    
'''
# function which return reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False
  
  
# Driver code 
s = "malayalam"
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") 
