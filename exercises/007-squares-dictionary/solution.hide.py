def squares_dictionary(n):
    return {number: number ** 2 for number in range(1, n + 1)}


# Try your function with different values
print(squares_dictionary(5))
