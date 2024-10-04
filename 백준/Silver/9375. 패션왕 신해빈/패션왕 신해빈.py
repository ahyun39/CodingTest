from collections import Counter

def solution():
    t = int(input())
    for _ in range(t):
        n = int(input())
        clothes = []
        for _ in range(n):
            _, clothes_cate = input().split()
            clothes.append(clothes_cate)
        
        clothes_count = Counter(clothes)
        ans = 1
        
        for count in clothes_count.values():
            ans *= (count + 1)
        
        ans -= 1
        
        print(ans)

if __name__ == "__main__":
    solution()