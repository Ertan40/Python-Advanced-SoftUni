n = int(input())
unique = set()

for _ in range(n):
    username = input()
    unique.add(username)
for username in unique:
    print(username)

