def dectobin(num):
    if num>1:
        dectobin(num//2)
    print(num%2,end=' ')
    
    
    return num
num=int(input('enter the no'))
dectobin(num)

      
      
    
    
