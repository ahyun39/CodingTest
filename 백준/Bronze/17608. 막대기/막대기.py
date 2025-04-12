import sys

def count_visible_sticks(heights):
    max_height = 0
    count = 0

    for height in reversed(heights):  # 오른쪽에서 왼쪽으로
        if height > max_height:
            count += 1
            max_height = height
    return count

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    heights = [int(input()) for _ in range(N)]
    print(count_visible_sticks(heights))