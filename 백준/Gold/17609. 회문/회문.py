def main():
    T = int(input())
    
    def is_palindrome(word):
        l, r = 0, len(word) - 1
        while l < r:
            if word[l] == word[r]:
                l += 1
                r -= 1
            else:
                # 왼쪽 문자 제거 시도
                if is_palindrome_after_removal(word, l + 1, r):
                    return 1  # 유사 팰린드롬
                # 오른쪽 문자 제거 시도
                if is_palindrome_after_removal(word, l, r - 1):
                    return 1  # 유사 팰린드롬
                return 2  # 팰린드롬 아님
        return 0  # 완전한 팰린드롬
    
    def is_palindrome_after_removal(word, left, right):
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True
    
    for _ in range(T):
        word = input()
        result = is_palindrome(word)
        print(result)

if __name__ == "__main__":
    main()