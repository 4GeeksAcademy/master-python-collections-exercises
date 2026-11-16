def binary_divisible_by_five(text):
    return [binary for binary in text.split(",") if int(binary, 2) % 5 == 0]


# Try your function with different values
print(binary_divisible_by_five('0100,0011,1010,1001'))
