def count_letters_and_digits(text):
    counts = {"letters": 0, "digits": 0}
    for char in text:
        if char.isalpha():
            counts["letters"] += 1
        elif char.isdigit():
            counts["digits"] += 1
    return counts


# Try your function with different values
print(count_letters_and_digits('hello world! 123'))
