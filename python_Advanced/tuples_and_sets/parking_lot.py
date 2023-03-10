number_of_commands = int(input())
parking_lot = set()

for _ in range(number_of_commands):
    direction, plate_number = input().split(", ")
    if direction == "IN":
        parking_lot.add(plate_number)
    if direction == "OUT":
        parking_lot.remove(plate_number)

if len(parking_lot) > 0:
    for plate_number in parking_lot:
        print(plate_number)
else:
    print("Parking Lot is Empty")


# number_of_commands = int(input())
# parking_lot = []
# left_parking_lot = []
# for _ in range(number_of_commands):
#     direction, car_number = input().split(", ")
#     if direction == "IN":
#         parking_lot.append(car_number)
#     else:
#         left_parking_lot.append(car_number)
#
# inside = set(i for i in parking_lot)
# outside = set(i for i in left_parking_lot)
# final_result = inside.symmetric_difference(outside)
#
# if len(final_result) > 0 and len(inside) != len(outside):
#     for num in final_result:
#         print(num)
#
# if len(inside) == len(outside):
#     print("Parking Lot is Empty")