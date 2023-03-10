from collections import deque
kids = deque(input().split())
toss = int(input())

counter = 1
while len(kids) > 1:
    kid = kids.popleft()
    if counter == toss:
        print(f"Removed {kid}")
        counter = 1
    else:
        counter += 1
        kids.append(kid)
winner = kids.popleft()
print(f"Last is {winner}")

