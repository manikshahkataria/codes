

def bouandary(mat,R,C):
    bsum=0
    for i in range(R):
        for j in range(C):
            if(i==0):
                print(mat[i][j],end='')
                bsum +=mat[i][j]
            elif(i==R-1):
                print(mat[i][j],end='')
                bsum +=mat[i][j]
            elif(j==0):
                print(mat[i][j],end='')
                bsum +=mat[i][j]
            elif(j==C-1):
                print(mat[i][j],end='')
                bsum +=mat[i][j]
            else:
                print(' ',end='')
        
        print( )       
    print('bouandary element sum', bsum)    



R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
mat = [[int(input()) for x in range (C)] for y in range(R)] 
 
for i in range(R):
    for j in range(C):
        print(mat[i][j],end=' ')
    print()


print('matrix')
print()

principal=0
secondary=0
if R==C:
    for i in range(0,R):
        principal +=mat[i][i]
        secondary +=mat[i][R-i-1]
    print('principal digonal',principal)
    print('secondary digonal',secondary)

print()
print()
bouandary(mat,R,C)#Boundary elements
