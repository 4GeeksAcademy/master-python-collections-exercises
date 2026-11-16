def common_elements(list_a, list_b):
    return sorted(set(list_a) & set(list_b))


# Try your function with different values
print(common_elements([5, 1, 3, 3, 8], [3, 8, 9, 5]))
