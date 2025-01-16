def binary_search(videos, M):
    left, right = max(videos), sum(videos)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        max_length, cnt = 0, 1 

        for video in videos:
            if max_length + video > mid:
                cnt += 1
                max_length = 0
            max_length += video

        if cnt <= M:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

def f():
    N, M = map(int, input().split())
    videos = list(map(int, input().split()))
    print(binary_search(videos, M))

f()
