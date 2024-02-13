r, c, w = map(int,input().split())
triangle = []
ans = 0
# 파스칼의 삼각형 생성
for i in range(r+w):
    row = [1] * (i+1) # 각 행의 처음과 끝은 1로 초기화
    for j in range(1,i):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)
# 정삼각형 내부 수들의 합
ans = sum([triangle[r+i-1][c+j-1] for i in range(w) for j in range(i+1)])
print(ans)