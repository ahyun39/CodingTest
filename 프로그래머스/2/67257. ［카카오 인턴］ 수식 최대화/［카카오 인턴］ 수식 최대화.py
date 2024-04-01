from itertools import permutations

def solution(expression):
    answer = 0
    expressions = []
    operators = []
    w = ""
    for i in range(len(expression)):
        if expression[i] not in ["-","+","*"]:
            w += expression[i]
        else:
            operators.append(expression[i])
            expressions.append(int(w))
            w = ""
    expressions.append(int(w))
    
    operator_set = set(operators)
    len_operator = len(operator_set)
    for operator in permutations(operator_set,len_operator):
        i = 0
        exp = expressions.copy()
        ope = operators.copy()
        while i < len_operator:
            while True:
                if operator[i] in ope:
                    idx = ope.index(operator[i])
                    if operator[i] == "*":
                        exp[idx:idx+2] = [exp[idx] * exp[idx+1]]
                    elif operator[i] == "+":
                        exp[idx:idx+2] = [exp[idx] + exp[idx+1]]
                    else:
                        exp[idx:idx+2] = [exp[idx] - exp[idx+1]]
                    ope.remove(ope[idx])
                else: break
            i += 1
        if abs(exp[0]) > answer: answer = abs(exp[0])
    return answer