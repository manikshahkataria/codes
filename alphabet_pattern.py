'''
import string

def main():
    N = int(input())
    
    alphabet = string.ascii_lowercase[:N]
    print(alphabet)
    
    height = N * 2 - 1
    width = N * 4 - 3
    lines = [None] * height
    print(lines)
    for i in range(N):
        sub_alphabet = alphabet[(-i - 1):]
        
        letters = ''.join(reversed(sub_alphabet)) + sub_alphabet[1:]
        lines[i] = lines[-i - 1] = '-'.join(letters).center(width, '-')
    
    print(*lines, sep='\n')

if __name__ == '__main__':
    main()
'''

import string

N = int(input())

mid = N - 1

for i in range(N - 1, 0, -1):
    row = ['-'] * (2 * N - 1)
    for j in range(N - i):
        row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
    print('-'.join(row))

for i in range(0, N):
    row = ['-'] * (2 * N - 1)
    for j in range(0, N - i):
        row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
    print('-'.join(row))
'''
import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))
'''
