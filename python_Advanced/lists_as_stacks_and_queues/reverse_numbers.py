# numbers = list(input())
# stack = []
#
# while len(numbers) > 0:
#     stack.append(numbers.pop())
#
# print("".join(stack))

numbers = input().split()
while numbers:
    print(numbers.pop(), end=" ")
