lines = int(input())
unique = set()

for _ in range(lines):
    elements = input()
    if len(elements.split()) == 1:
        unique.add(elements)
    elif(len(elements.split())) > 1:
        for element in elements.split():
            unique.add(element)

for e in unique:
    print(e)

# print(*my_list) # [['Ce', 'O'], ['Mo', 'O', 'Ce'], ['Ee'], ['Mo']]

# for elements in my_list:
#     if len(elements) > 1:
#         for el in elements:
#             unique.add(*el)
#
#     elif len(elements) == 1:
#         unique.add(*elements)
# print(unique)
# for _ in range(lines):
#     elements = tuple(input().split())
#     if len(elements) > 1:
#         for element in elements:
#             unique.add(element)
#     elif len(elements) == 1:
#         unique.add(elements)
#
# print(unique) # {'O', 'Mo', ('Ee',), 'Ce', ('Mo',)}

