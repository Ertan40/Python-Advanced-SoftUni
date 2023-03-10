number = int(input())
names_list = []

for _ in range(number):
    current_name = input()
    names_list.append(current_name)

unique = set(i for i in names_list)
print("\n".join(list(unique)))

# number = int(input())
# unique = set()
#
# for _ in range(number):
#     current_name = input()
#     unique.add(current_name)
#
# for name in unique:
#     print(name)