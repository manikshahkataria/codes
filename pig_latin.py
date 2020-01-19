ori=input('enter the word')
v=['a','e','i','o','u','y']
pig='aya'
ig='ay'

fi=ori[0]

for i in v:
    if (i==fi):
        word=ori+fi+pig
        word=word[1:]
        break

        
    else:
        word=ori+fi+ig
        word=word[1:]
print(word)

        
