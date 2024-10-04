def solution():
    k, l = map(int, input().split())
    class_student = {}
    start_idx = 0
    for _ in range(l):
        student_id = str(input())
        class_student[student_id] = start_idx
        start_idx += 1
    confirmed_student = [key for key, value in sorted(class_student.items(), key=lambda x:x[1])][:k]
    return confirmed_student
if __name__ == "__main__":
    print(*solution(), sep='\n')