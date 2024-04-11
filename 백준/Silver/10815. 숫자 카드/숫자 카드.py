def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return 0

n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
cards2 = list(map(int, input().split()))

ans = []
for card in cards2:
    ans.append(binary_search(cards, card))

print(*ans)