from bisect import bisect_left

def longest_increasing_subsequence():
    n = int(input())
    nums = list(map(int, input().split()))
    
    lis = []
    
    for num in nums:
        pos = bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
    
    print(len(lis))

if __name__ == "__main__":
    longest_increasing_subsequence()