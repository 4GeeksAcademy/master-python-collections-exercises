def two_dimensional_list(rows, columns):
    return [[i * j for j in range(columns)] for i in range(rows)]


# Try your function with different values
print(two_dimensional_list(3, 5))
