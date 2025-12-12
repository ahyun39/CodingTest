import sys
pre = list(map(int, sys.stdin.read().split()))
sys.setrecursionlimit(10000)

def preorder_to_postorder(pre):
    n = len(pre)
    idx = 0
    post = []

    def build(upper):
        nonlocal idx
        if idx == n or pre[idx] > upper:
            return
        root_val = pre[idx]
        idx += 1
        build(root_val)
        build(upper)
        post.append(root_val)
    
    build(float('inf'))
    return post

post = preorder_to_postorder(pre)
print(*post, end='\n')