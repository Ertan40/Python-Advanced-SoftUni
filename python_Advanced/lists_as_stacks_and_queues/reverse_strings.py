text = input()
text_as_list = list(text)
stack = []

while text_as_list: # len(text_as_list) > 0:
    stack.append(text_as_list.pop())
print("".join(stack))

# text = list(input()) # second_way
# while len(text) > 0:
#     print(text.pop(), end="")

# for i in text_as_list:
#     stack.append(i)
# print("".join(stack[::-1]))