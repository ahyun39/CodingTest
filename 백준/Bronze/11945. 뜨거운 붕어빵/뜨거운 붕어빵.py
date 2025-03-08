def main():
    N, M = map(int, input().split())
    bungeobbang = [str(input())[::-1] for _ in range(N)]
    print(*bungeobbang, sep='\n')

if __name__ == "__main__":
    main()