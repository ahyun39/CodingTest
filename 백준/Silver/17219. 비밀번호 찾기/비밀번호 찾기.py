n, m = map(int,input().split())
passwords = {}

for _ in range(n):
    site, password = map(str,input().split())
    passwords[site] = password

for _ in range(m):
    site = str(input())
    print(passwords[site])