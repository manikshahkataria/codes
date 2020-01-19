import math
t=int(input('test'))
c=0
od=[]
for i in range(t):
    d=int(input('door'))
    for i in range(1,d+1):
        
        
        n=int(math.sqrt(i))
        if (i==n*n):
            print(i,"perfect")
            c+=1
    print(c)        














'''if door no has even no of factor the final result will be close
eg 50 factors=1 2 5 10 25 50 has six factor even no final state will be close
        close=o c o c   o  close
    odd no of factor will be open we need to find that

                      door no50
                1   2    5      10   25    50
                1x50=50
even no factor  2x25
                5x10

                      36  
          1  2  3  4  6  9  12  18  36   odd no of factor has perfect square                         

                6x6=36






                        

        '''     
