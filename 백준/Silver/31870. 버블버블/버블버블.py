n = int(input())
a = list(map(int,input().split()))

def bubble_sort(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return swap_count

original_swaps = bubble_sort(a[:])

reversed_a = a[::-1]
reverse_swaps = bubble_sort(reversed_a)

min_swaps = min(original_swaps, reverse_swaps + 1)

print(min_swaps)