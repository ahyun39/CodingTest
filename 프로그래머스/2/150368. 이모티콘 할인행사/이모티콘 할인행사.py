from itertools import product

def solution(users, emoticons):
    answer = []
    arr = [0.6,0.7,0.8,0.9]
    n = len(emoticons)
    emo_plus = 0
    pay = []
    for i in product(arr,repeat=n):
        discount = [round(x*y) for x,y in zip(list(i),emoticons)]
        for j in users:
            user_pay = 0
            for t in range(len(list(i))):
                if j[0] <= 100 - ((list(i)[t])*100):
                    user_pay += discount[t]
            if user_pay < j[1]:
                pay.append(user_pay)
            elif user_pay >= j[1]:
                emo_plus += 1
        answer.append([emo_plus,sum(pay)])
        pay = []
        emo_plus = 0
    answer = sorted(answer,key = lambda x : (x[0],x[1]),reverse=True)
    return answer[0]