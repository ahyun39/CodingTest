def recruit():
    N = int(input())
    applicants = [list(map(int, input().split())) for _ in range(N)]
    applicants.sort()

    max_new = 0
    min_b = float('inf')

    for _, b in applicants:
        if b < min_b:  # 현재 b가 지금까지의 최소값보다 작으면 새로운 그룹 가능
            max_new += 1
            min_b = b  # 최소값 업데이트

    return max_new

def main():
    T = int(input())
    for _ in range(T):
        print(recruit())

if __name__ == "__main__":
    main()