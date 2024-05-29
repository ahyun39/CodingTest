import itertools, copy

N, M, K = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]
g = []
for _ in range(K):
    g.append(list(map(int,input().split())))
permu = list(itertools.permutations(g,K))
score = []

def locat(now_l, now_r, pp):
    temp = pp[now_l[0]-1][now_l[1]-1]
    for i in range(now_l[0],now_r[0]): # up
        pp[i-1][now_l[1]-1] = pp[i][now_l[1]-1]
    for i in range(now_l[1],now_r[1]): # left
        pp[now_r[0]-1][i-1] = pp[now_r[0]-1][i]
    for i in range(now_r[0], now_l[0],-1): # down
        pp[i-1][now_r[1]-1] = pp[i-2][now_r[1]-1]
    for i in range(now_r[1], now_l[1]+1,-1): # right
        pp[now_l[0]-1][i-1] = pp[now_l[0]-1][i-2]
    pp[now_l[0]-1][now_l[1]] = temp
    return

def sco(pp):
    _score = []
    for i in range(N):
        _score.append(sum(pp[i]))
    score.append(min(_score))


for z in range(len(permu)):
    pp = copy.deepcopy(mapp)
    for j in range(K):
            r, c, s = permu[z][j][0], permu[z][j][1], permu[z][j][2]
            for h in range((2*s + 1)//2):
                now_l = (r-s+h, c-s+h)
                now_r = (r+s-h, c+s-h)
                locat(now_l, now_r,pp)
    sco(pp)

print(min(score))