l=[]
def permutations(string, step = 0):
    if step == len(string) and string!=None and l.count("".join(string))==0:
        l.append("".join(string))
        # we've gotten to the end, print the permutation
        

    for i in range(step, len(string)):
        # copy the string (store as array)
        string_copy = [c for c in string]
         # swap the current index with the step
        string_copy[step], string_copy[i] =string_copy[i], string_copy[step]
         # recurse on the portion of the stringthat has not been swapped yet
        permutations(string_copy, step + 1)
#permutations('man')
n=input('enter string')
permutations(n)

p=[]


c=0
for i in list(l):
    
    if (i==i[::-1]):
        
            c=c+1
    else:
            c=c
if c>0:
    print('anidrom')
else:
    print('not anidrom')
