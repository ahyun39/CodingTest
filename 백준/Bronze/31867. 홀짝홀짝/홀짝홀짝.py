n = int(input()) # 자릿수
k = str(input()) # 자연수
odd, even = 0, 0
for i in range(n):
    if int(k[i]) % 2 == 0: even += 1
    else: odd += 1
print(0 if even > odd else 1 if even < odd else -1)