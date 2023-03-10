lines = int(input())
# "{first_start},{first_end}-{second_start},{second_end}"    0,3-1,2
first_nums = set()
second_nums = set()
combined_intersection = set()
max_intersection = 0

for _ in range(lines):
    data = input().split("-") # ['6,15', '3,10']
    first_start, first_end = data[0].split(",") # range_1 = [int(i) for i in data[0].split(",")]
    second_start, second_end = data[1].split(",") # range_2 = [int(i) for i in data[1].split(",")]

    if first_start.isalnum() and first_end.isalnum() and second_start.isalnum() and second_end.isalnum():
        for i in range(int(first_start), int(first_end) + 1):
            first_nums.add(i)
        for i in range(int(second_start), int(second_end) + 1):
            second_nums.add(i)
        sets_intersections = first_nums.intersection(second_nums)

        if len(sets_intersections) > max_intersection:
            max_intersection = len(sets_intersections)
            combined_intersection = sets_intersections
        first_nums.clear()
        second_nums.clear()

my_list = []
for num in combined_intersection:
    my_list.append(num)

print(f"Longest intersection is {my_list} with length {max_intersection}")

####################### second_way #############################

# lines = int(input())
# longest_intersection = set()
#
# for _ in range(lines):
#     first_data, second_data = [el.split(",") for el in input().split("-")]
#
#     first_range = set(range(int(first_data[0]), int(first_data[1]) + 1))
#     second_range = set(range(int(second_data[0]), int(second_data[1]) + 1))
#
#     intersection = first_range.intersection(second_range)
#     if len(longest_intersection) < len(intersection):
#         longest_intersection = intersection
#
# print(
#     f"Longest intersection is "
#     f"[{', '.join(str(i) for i in longest_intersection)}] "
#     f"with length {len(longest_intersection)}"
# )




