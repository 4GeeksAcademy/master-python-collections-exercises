def square_odd_numbers(text):
    return [int(n) ** 2 for n in text.split(",") if int(n) % 2 != 0]


# Try your function with different values
print(square_odd_numbers('1,2,3,4,5,6,7,8,9'))
