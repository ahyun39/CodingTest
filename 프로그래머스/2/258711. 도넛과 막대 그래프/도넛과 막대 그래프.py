from collections import defaultdict

def solution(edges):
    answer = [0,0,0,0]
    dic = defaultdict(lambda:[0,0])
    
    for i, j in edges:
        dic[i][0] += 1 # 나가는 간선
        dic[j][1] += 1 # 들어오는 간선
        
    for node, item in dic.items():
        out_ = item[0]
        in_ = item[1]
        if out_ >= 2 and in_ == 0: answer[0] = node
        elif out_ >= 2 and in_ >= 2: answer[3] += 1
        elif out_ == 0 and in_ >= 1: answer[2] += 1
        
    t = dic[answer[0]][0] # 생성한 정점에 연결된 그래프
    answer[1] = t - answer[2] - answer[3]
    return answer