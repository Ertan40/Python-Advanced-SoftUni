numbers = list(map(int, input().split(", ")))
index = int(input())

cycles = 0
job_to_get_done = numbers[index]

while job_to_get_done in numbers:
    cycles += min(numbers)
    numbers.remove(min(numbers))
print(cycles)