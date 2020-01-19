try:
    from itertools import permutation
except ImportError:
    from itertools import permutation as permutation
    
def allpermutation(str):
    perlist= permutation(str)
    for perm in list(perlist):
        print(''.join(perm))
if __name__=="__main__":
    str='abc'
    allpermutation(str)

'''try:
    # Python 3
    from itertools import zip_longest
except ImportError:
    # Python 2
    from itertools import izip_longest as zip_longest
'''
