def flatten(nested):
    return [value for row in nested for value in row]


# Try your function with different values
print(flatten([[1, 2], [3], [], [4, 5, 6]]))
