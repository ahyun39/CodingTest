def hanoi(n, start, aux, end, moves):
    if n == 0:
        return
    hanoi(n - 1, start, end, aux, moves)   # 위 n-1개를 보조로
    moves.append((start, end))             # 가장 큰 1개를 목표로
    hanoi(n - 1, aux, start, end, moves)   # 보조의 n-1개를 목표로

def main():
    import sys
    input = sys.stdin.readline
    n = int(input().strip())
    moves = []
    hanoi(n, 1, 2, 3, moves)
    out_lines = [str(len(moves))]
    out_lines += [f"{a} {b}" for a, b in moves]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()