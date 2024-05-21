j, i = map(int,input().split())
# 준성이가 이기는 경우
if (j == 0 and i == 2) or (j == 2 and i == 5) or (j == 5 and i == 0):
    print(">")
# 익준이가 이기는 경우
elif (j == 0 and i == 5) or (j == 2 and i == 0) or (j == 5 and i == 2):
    print("<")
# 둘 중 한명이 무효를 내는 경우
elif (j not in [0,2,5] and i in [0,2,5]):
    print("<")
elif (j in [0,2,5] and i not in [0,2,5]):
    print(">")
else:
    print("=")