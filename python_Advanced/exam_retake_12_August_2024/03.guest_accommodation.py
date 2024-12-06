def accommodate(*args, **kwargs):
    # ((5, 4, 2), {'room_305': 6, 'room_410': 5, 'room_204': 2})
    # [('room_204', 2), ('room_410', 5), ('room_305', 6)]
    guest_groups = list(args)
    available_rooms = kwargs
    unaccommodated_guests = 0
    successful_accommodations = {}

    # Sort rooms by capacity and room number
    sorted_rooms = sorted(available_rooms.items(), key=lambda x: (x[1], x[0]))
    for group_size in guest_groups:
        accommodated = False
        for room, capacity in sorted_rooms:
            if group_size <= capacity:
                room_number = room.split("_")[1]
                # Accommodate the group in the room
                if room_number not in successful_accommodations:
                    successful_accommodations[room_number] = group_size
                    sorted_rooms.remove((room, capacity))  # Remove room after use
                    accommodated = True
                    break
        if not accommodated:
            unaccommodated_guests += group_size

    output = []

    if successful_accommodations:  # If any accommodations were completed
        output.append(f"A total of {len(successful_accommodations)} accommodations were completed!")
        for room_number in sorted(successful_accommodations.keys()):
            output.append(f"<Room {room_number} accommodates {successful_accommodations[room_number]} guests>")
    else:  # If no accommodations were completed
        output.append("No accommodations were completed!")

    if unaccommodated_guests > 0:
        output.append(f"Guests with no accommodation: {unaccommodated_guests}")

    if sorted_rooms:
        output.append(f"Empty rooms: {len(sorted_rooms)}")

    return "\n".join(output).strip()


# Test cases
print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))