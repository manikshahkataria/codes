import operator

n = int( input('enter no' ) )
r = []
for i in range( n ):
    name  = input('name' )
    score = float( input('marks' ) )
    r.append( [ name, score ] )
    
r = sorted( r, key = operator.itemgetter( 1, 0 ) )
print(r)
for s in r:
    if s[1] != r[0][1]:
        print(s)
        smin = s[1]
        break

for s in r:
    if s[1] == smin:
        print( s[0] )
        
