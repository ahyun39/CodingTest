from collections import deque 

wheels = [deque(input()) for _ in range(4)]
k = int(input())
for _ in range(k):
    wheel_num, direction = map(int, input().split())
    wheel_num -= 1
    
    rotations = [0] * 4
    rotations[wheel_num] = direction
    
    for i in range(wheel_num, 3):
        if wheels[i][2] != wheels[i+1][6]:
            rotations[i+1] = -rotations[i]
        else:
            break
            
    for i in range(wheel_num, 0, -1):
        if wheels[i][6] != wheels[i-1][2]:
            rotations[i-1] = -rotations[i]
        else:
            break
            
    for i in range(4):
        wheels[i].rotate(rotations[i])

print(sum(int(wheels[i][0]) * (1 << i) for i in range(4)))