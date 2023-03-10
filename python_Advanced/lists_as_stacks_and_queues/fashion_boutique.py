clothes = list(map(int, input().split()))
capacity = int(input())
total = 0
rack_counter = 1

for _ in range(len(clothes)):
    if total + clothes[-1] > capacity:
        rack_counter += 1
        total = clothes.pop()
    elif total + clothes[-1] == capacity:
        total = 0
        clothes.pop()
        if clothes:
            rack_counter += 1
    else:
        total += clothes.pop()
print(rack_counter)

# clothes = input().split()
# capacity = int(input())
# stack = []
# total = 0
# rack_counter = 1
# 
# for num in clothes:
#     stack.append(int(clothes.pop()))
#     total += sum(stack)
#     if total == capacity:
#         total = 0
#         if clothes:
#             rack_counter += 1
#             stack.clear()
#     elif total > capacity:
#         rack_counter += 1
#         stack.clear()
#         total = 0
# print(rack_counter)
