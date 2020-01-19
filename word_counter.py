s=input().strip()
wordcount={char: s.count(char) for char in s}
print(wordcount)
for k,v in wordcount.items():
    print(k,":",v)
