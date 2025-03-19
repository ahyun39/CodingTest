from collections import defaultdict

def main():
    N = int(input())
    words = [input().strip() for _ in range(N)]
    
    prefix_map = defaultdict(list)
    
    # 해시맵을 사용하여 prefix별로 단어를 그룹화
    for word in words:
        for i in range(1, len(word) + 1):
            if len(prefix_map[word[:i]]) < 2:
                prefix_map[word[:i]].append(word)

    max_length = 0
    max_words = []
    
    # 가장 긴 접두사를 찾음
    for prefix, prefix_words in prefix_map.items():
        if len(prefix_words) > 1 and len(prefix) > max_length:
            max_length = len(prefix)
            max_words = prefix_words
    
    return max_words

if __name__ == "__main__":
    print(*main(), sep='\n')