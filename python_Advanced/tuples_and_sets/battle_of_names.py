lines = int(input())
odd_nums_set = set()
even_nums_set = set()
row_counter = 1

for _ in range(lines):
    current_name = input().strip()
    sum_of_current_name = 0
    for ch in current_name:
        sum_of_current_name += int(ord(ch))
    final_sum = int(sum_of_current_name)/row_counter
    row_counter += 1
    if int(final_sum) % 2 != 0:
        odd_nums_set.add(int(final_sum))
    else:
        even_nums_set.add(int(final_sum))

if sum(odd_nums_set) == sum(even_nums_set):
    union = odd_nums_set.union(even_nums_set)
    print(*union, sep=", ")
elif sum(odd_nums_set) > sum(even_nums_set):
    difference = odd_nums_set.difference(even_nums_set)
    print(*difference, sep=", ")
elif sum(odd_nums_set) < sum(even_nums_set):
    symmetric_difference = odd_nums_set.symmetric_difference(even_nums_set)
    print(*symmetric_difference, sep=", ")