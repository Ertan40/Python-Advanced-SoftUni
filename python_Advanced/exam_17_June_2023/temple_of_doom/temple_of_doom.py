from collections import deque

# tools = [int(t) for t in input().split()]
tools = deque(list(map(int, input().split())))  # deque([2, 4, 6, 8])
substances = [int(s) for s in input().split()]   # [11, 3, 5, 7, 9]
challenges = [int(c) for c in input().split()]   # [24, 28, 18, 30]

while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()
    challenge = tool * substance
    if challenge in challenges:
        challenges.remove(challenge)
    else:
        tools.append(tool + 1)
        last_sub = substance - 1
        if last_sub == 0:
            continue
        else:
            substances.append(last_sub)

if not substances:
    if tools or challenges:
        print(f"Harry is lost in the temple. Oblivion awaits him.")

if not challenges:
    print(f"Harry found an ostracon, which is dated to the 6th century BCE.")


if tools:
    print(f"Tools: {', '.join(str(t) for t in tools)}")

if substances:
    print(f"Substances: {', '.join(str(s) for s in substances)}")

if challenges:
    print(f"Challenges: {', '.join(str(c) for c in challenges)}")
