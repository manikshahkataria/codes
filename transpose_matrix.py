def transpose(mat,b):
    for i in range(r):
        for j in range(c):
            b[i][j]=mat[j][i]
r=int(input('row'))
c=int(input('col'))
mat=[[int(input()) for x in range(r)] for y in range(c)]
for i in range(r):
    for j in range(c):
        print(mat[i][j],end=' ')
    print()

b=[[0 for x in range(r)] for y in range(c)]
transpose(mat,b)
for i in range(r):
    for j in range(c):
        print(b[i][j],end=' ')
    print()
