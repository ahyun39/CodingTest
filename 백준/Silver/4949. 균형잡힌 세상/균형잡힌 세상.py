while True:
    string = str(input())
    if string == '.':
        break
    brackets = []
    for i in range(len(string)-1):
        if string[i] == "(" or string[i] == "[":
                brackets.append(string[i])
        elif string[i] == ")":
                if brackets:
                    if brackets[-1] == "(":
                        brackets.pop()
                    else:
                        break
                else:
                    brackets.append(string[i])
                    break
        elif string[i] == "]":
                if brackets:
                    if brackets[-1] == "[":
                        brackets.pop()
                    else:
                        break
                else:
                    brackets.append(string[i])
                    break
    if string[-1] != ".":
        print("no")
    else:
        if brackets:
            print("no")
        else:
            print("yes")