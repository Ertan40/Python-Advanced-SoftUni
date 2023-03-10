################################ judge = 80 ######################################
stack = []
number = int(input())

for num in range(number):
    query = input().split()

    if len(query) == 2:
        stack.append(int(query[1])) # stack.append(stack.pop(int(query[1])))
    else:
        if int(query[0]) == 2 and len(stack) > 0:
            stack.pop()
        elif int(query[0]) == 3:
            print(max(stack))
        elif int(query[0]) == 4:
            print(min(stack))
into_string = [str(i) for i in stack]
print(", ".join(into_string[::-1]))
################################ judge = 100 ######################################
# from collections import deque
# numbers = deque()
#
# map_functions = {
#     1: lambda x: numbers.append(x[1]),
#     2: lambda x: numbers.pop() if numbers else None,
#     3: lambda x: print(max(numbers)) if numbers else None,
#     4: lambda x: print(min(numbers)) if numbers else None,
# }
# for _ in range(int(input())):
#     number_data = [int(num) for num in input().split()]
#     map_functions[number_data[0]](number_data)
#
# numbers.reverse()
# # print(numbers) => deque([91, 20, 26]) # print(*numbers) => 91 20 26
# print(*numbers, sep=", ")  # 91, 20, 26
