def main():
    T = int(input())

    for _ in range(T):
        R, S = map(str, input().split())
        P = ""
        for s in S:
            P += s * int(R)
        print(P)

if __name__ == "__main__":
    main()