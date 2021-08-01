axis_direction = [-1, 0, 1]
possible_directions = []

for direction_x in axis_direction:
    for direction_y in axis_direction:
        if (direction_x, direction_y) != (0, 0):
            possible_directions.append((direction_x, direction_y))
