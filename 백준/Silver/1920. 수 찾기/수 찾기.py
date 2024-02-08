N, N_set, M, M_list = int(input()), set(map(int, input().split())), int(input()), list(map(int, input().split()))
print(*[1 if num in N_set else 0 for num in M_list], sep='\n')