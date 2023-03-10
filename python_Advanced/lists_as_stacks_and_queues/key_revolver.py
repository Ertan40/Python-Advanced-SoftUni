price_of_each_bullet = int(input())
size = int(input())
bullets = list(map(int, input().split())) # [11, 10, 5, 11, 10, 20]
locks = list(map(int, input().split())) # [15, 13, 16]
value_of_the_intelligence = int(input())
tracker = 0
bullet_tracker = 0
locks.reverse() # [16, 13, 15]

while locks and bullets:
    current_bullet = bullets.pop()
    current_lock = locks.pop()
    bullet_tracker += 1
    if current_bullet <= current_lock:
        print("Bang!")
        tracker += 1
    else:
        locks.append(current_lock)
        print("Ping!")
        tracker += 1
    if tracker == size and bullets:
        print("Reloading!")
        tracker = 0
money_earned = value_of_the_intelligence - bullet_tracker * price_of_each_bullet

if bullets or len(bullets) == 0 and len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

# print(bullets) # [11, 10]
# print(locks)   # []