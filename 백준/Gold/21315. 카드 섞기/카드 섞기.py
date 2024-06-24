n = int(input())
input_cards = list(map(int,input().split()))

def mix_card(cards,i,k):
    if i > k + 1:
        return cards
    if i == 1:
        cnt = 2 ** k
    else:
        cnt = 2 ** (k-i+1)
    l = len(cards)
    next = cards[l - cnt:]
    return mix_card(next, i+1, k) + cards[:l - cnt]

def solve():
    f = 1
    while 2 ** f < n:
        first = mix_card([i for i in range(1,n+1)], 1, f)
        s = 1
        while 2 ** s < n:
            second = mix_card(first, 1, s)
            if second == input_cards:
                print(f, s)
                return
            s += 1
        f += 1
solve()