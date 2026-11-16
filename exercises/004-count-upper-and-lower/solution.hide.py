def count_upper_and_lower(text):
    counts = {"uppercase": 0, "lowercase": 0}
    for char in text:
        if char.isupper():
            counts["uppercase"] += 1
        elif char.islower():
            counts["lowercase"] += 1
    return counts


# Try your function with different values
print(count_upper_and_lower('Hello world!'))
