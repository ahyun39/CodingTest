n, k = map(int,input().split())
scores = list(map(int,input().split()))
scores.sort(key=lambda x:-x)
print(scores[k-1])