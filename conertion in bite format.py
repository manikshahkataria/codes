from struct import *
packed=pack('iif',6,19,4.12)
print(packed)
print(calcsize('i'))
print(calcsize('e'))
orignal=unpack('iif',packed)
print(orignal)
print(unpack('fif',b'\x06\x00\x00\x00\x13\x00\x00\x00\n\xd7\x83@'))
;pp0l.
