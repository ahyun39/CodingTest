def main():
    for _ in range(int(input())):
        R, S = input().split()
        print(''.join(s * int(R) for s in S))

if __name__ == "__main__":
    main()