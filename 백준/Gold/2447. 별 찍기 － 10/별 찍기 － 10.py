def draw_stars(n):
    if n == 3:
        return ["***", "* *", "***"]
    sub_pattern = draw_stars(n // 3)
    result = []
    for i in range(n):
        if i // (n // 3) == 1:
            result.append(sub_pattern[i % (n // 3)] + ' ' * (n // 3) + sub_pattern[i % (n // 3)])
        else:
            result.append(sub_pattern[i % (n // 3)] * 3)
    return result

def print_stars(n):
    pattern = draw_stars(n)
    for line in pattern:
        print(line)

n = int(input())
print_stars(n)