def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
result=greatest(a=input('first no'),b=input('second no'),c=input('third no'))

print('greatest is'+str(result))
