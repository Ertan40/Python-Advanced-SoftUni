#-------------------------- judge 87 points  -----------------------------------------------
from collections import deque
food_portions = [int(x) for x in input().split(", ")]   # food_portions.pop() or food_portions[-1]
quantities = deque([int(x) for x in input().split(", ")])  # quantities.popleft() or quantities[0]
peaks = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
conquered_peaks = []
failed_condition = False

for peak, difficult in peaks.items():
    while True:
        food_portion = food_portions.pop()
        quantity = quantities.popleft()
        daily_sum = food_portion + quantity
        if daily_sum >= difficult:
            conquered_peaks.append(peak)
            break
        elif len(food_portions) == 0 or len(quantities) == 0:
            failed_condition = True
            break
    if failed_condition:
        if len(conquered_peaks) == 0:
            print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
            break
if not failed_condition:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
if conquered_peaks:
    result = '\n'.join(conquered_peaks)
    print("Conquered peaks:")
    print(f"{result}")

