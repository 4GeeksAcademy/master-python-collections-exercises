def all_digits_even(start, end):
    return [
        number
        for number in range(start, end + 1)
        if all(int(digit) % 2 == 0 for digit in str(number))
    ]


# Try your function with different values
print(all_digits_even(2000, 2030))
