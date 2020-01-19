
def reverse(s):
    return s[::-1]


def palindrom(s):
    rev=reverse(s)
    if(s==rev):
        return True
    else:
        return False


s='madam'
pali=palindrom(s)
if pali==True:
    print('yes')
else:
    print('no')
