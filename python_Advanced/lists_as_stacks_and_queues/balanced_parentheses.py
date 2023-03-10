parentheses = input()
stack = []
flag = True
for p in parentheses:
    if p in ['{', '[', '(']: # ['{', '[', '(']
        stack.append(p)
    elif p == "}":
        if stack and stack[-1] == "{":
            stack.pop()
        else:
            flag = False
            break
    elif p == "]":
        if stack and stack[-1] == "[":
            stack.pop()
        else:
            flag = False
            break
    elif p == ")":
        if stack and stack[-1] == "(":
                stack.pop()
        else:
            flag = False
            break
print("YES" if flag else "NO")

