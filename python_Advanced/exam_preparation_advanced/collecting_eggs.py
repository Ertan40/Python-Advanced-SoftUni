from collections import deque
eggs = deque(list(map(int, input().split(", "))))  # eggs.popleft() or eggs[0]
papers = list(map(int, input().split(", ")))  # papers.pop() or papers[-1]
box = 50
collected_eggs = []

while papers and eggs:
    egg = eggs[0]    # eggs.popleft()
    paper = papers[-1]    # papers.pop()
    wrapped_egg = egg + paper
    if egg <= 0:
        eggs.popleft()
        continue
    if egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        eggs.popleft()
        continue
    if wrapped_egg <= box:
        collected_eggs.append(wrapped_egg)
        eggs.popleft()
        papers.pop()
    if wrapped_egg > box:
        eggs.popleft()
        papers.pop()
        continue

if collected_eggs:
    print(f"Great! You filled {len(collected_eggs)} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join([str(e) for e in eggs])}")
if papers:
    print(f"Pieces of paper left: {', '.join([str(p) for p in papers])}")
