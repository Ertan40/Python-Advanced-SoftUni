n, m = input().split() # n, m = [int(digit) for digit in input().split()]

first_set = set()
second_set = set()

for _ in range(int(n)):
    current_num = int(input())
    if len(first_set) < int(n):
        first_set.add(current_num)
for _ in range(int(m)):
    current_num = int(input())
    if len(second_set) < int(m):
        second_set.add(current_num)

repeated_elements = first_set.intersection(second_set)
for rep in repeated_elements:
    print(rep)
