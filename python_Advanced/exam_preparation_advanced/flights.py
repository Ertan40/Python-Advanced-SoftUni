def flights(*args):
    # ('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15)
    data = list(args)
    flights = {}
    while data:
        new_entry = data.pop(0)
        if new_entry == "Finish":
            break
        else:
            destination = new_entry
            passengers = int(data.pop(0))
            if destination not in flights:
                flights[destination] = 0
            flights[destination] += passengers
    return flights



print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))