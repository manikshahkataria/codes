import sys
n= int(sys.stdin.readline().strip()) #how many entries in dict
phone_book= dict()
for i in range(n):
    entry=sys.stdin.readline().strip().split(' ') #ip entry
    phone_book[entry[0]]=entry[1]#entry [0] pr key=name,entry [1] pr no
    #print(entry[0])
    
query= sys.stdin.readline().strip()#dict me search krne ke lea ,jis nam ka no chiye
#print(query)
while query:
    phone_num= phone_book.get(query) #if name exists in dict 
    if phone_num:
        print(query + '=' + phone_num)
    else:
        print('Not found')
    query= sys.stdin.readline().strip() #continusly or query lete rehne ke lea
