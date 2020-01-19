a=int(input('enter the selling price'))
b=int(input('enter the cost price'))
c=0
if a>b:
    c=float((a-b)/100)*100
    print(c,"is % of profit")
else:
    c=float((b-a)/100)*100
    print(c,"is % of loss")
    
