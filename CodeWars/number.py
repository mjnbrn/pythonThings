def number(bus_stops):
    passengers = 0
    for t in bus_stops:
        passengers += t[0]
        passengers -= t[1]
    return passengers

cla

number([[10, 0], [3, 5], [5, 8]])
number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]])
number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]])
