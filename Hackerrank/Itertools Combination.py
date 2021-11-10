from itertools import combinations

s , n  = input().split()

s = sorted(s)

for i in range(1, int(n)+1):
    for j in combinations(s, i):
        print(''.join(j))