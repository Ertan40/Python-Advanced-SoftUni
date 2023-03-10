line = list(map(int, input().split()))
negatives = []
positives = []
for num in line:
    if num < 0:
        negatives.append(num)
    else:
        positives.append(num)

print(sum(negatives))
print(sum(positives))
without_minus = (-1) * sum(negatives)

if without_minus > sum(positives):
    print(f"The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")