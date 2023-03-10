expression = input()
stack = []

for idx in range(len(expression)):
    ch = expression[idx]
    if ch == '(':
        stack.append(idx)
    elif ch == ")":
        last_idx = stack.pop()
        print(expression[last_idx:idx + 1])
