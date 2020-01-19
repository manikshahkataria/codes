r=int(input("enter row "))
c=int(input("enter col"))
def rotate(mat):
    mat=mat[::-1]
    for i in range(len(mat)):
        for j in range(i):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    return(mat)

mat=[[int(input()) for x in range(c)] for y in range(r)]

for i in range(r):
     for j in range(c):
         print(mat[i][j],end=' ')
     print()
     
print(mat)
#mat=mat[::-1]
#print("reversed matrix")
#print(mat)
for i in mat:
    print(i)
print()
print("90 degree")
print(rotate(mat))
