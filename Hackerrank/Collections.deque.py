from collections import deque

d = deque()

for _ in range(int(input())):
    method, *n = input().split()
    getattr(d, method)(*n)

print(*d)