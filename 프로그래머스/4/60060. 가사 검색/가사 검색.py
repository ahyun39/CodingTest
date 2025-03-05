class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
    
    def count_match(self, query):
        # 전체 와일드카드 처리
        if set(query) == {'?'}:
            return self.root.count
        
        node = self.root
        for char in query:
            if char == '?':
                break
            if char not in node.children:
                return 0
            node = node.children[char]
        
        return node.count if node else 0

def solution(words, queries):
    tries = {}
    tries_reverse = {}
    length_words = {}  # 길이별 단어 개수 저장
    
    # 단어들을 정방향 및 역방향 Trie에 삽입
    for word in set(words):
        length = len(word)
        
        # 길이별 단어 개수 저장
        length_words[length] = length_words.get(length, 0) + 1
        
        if length not in tries:
            tries[length] = Trie()
            tries_reverse[length] = Trie()
        
        tries[length].insert(word)
        tries_reverse[length].insert(word[::-1])
    
    # 각 쿼리에 대해 매칭되는 단어 수 계산
    result = []
    for query in queries:
        length = len(query)
        
        # 전체 와일드카드 처리
        if set(query) == {'?'}:
            result.append(length_words.get(length, 0))
            continue
        
        # 와일드카드 접두사인 경우
        if query[0] == '?':
            if length not in tries_reverse:
                result.append(0)
                continue
            
            reversed_query = query[::-1]
            match_count = tries_reverse[length].count_match(reversed_query)
            result.append(match_count)
        
        # 와일드카드 접미사인 경우
        else:
            if length not in tries:
                result.append(0)
                continue
            
            match_count = tries[length].count_match(query)
            result.append(match_count)
    
    return result