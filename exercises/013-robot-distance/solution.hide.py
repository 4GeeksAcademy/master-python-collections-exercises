import math


def robot_distance(movements):
    x = 0
    y = 0
    for movement in movements:
        direction, steps = movement.split()
        steps = int(steps)
        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps
    return round(math.sqrt(x ** 2 + y ** 2))


# Try your function with different values
print(robot_distance(['UP 5', 'DOWN 3', 'LEFT 3', 'RIGHT 2']))
