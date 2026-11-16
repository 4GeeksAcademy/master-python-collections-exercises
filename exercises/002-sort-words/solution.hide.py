def sort_words(text):
    return ",".join(sorted(text.split(",")))


# Try your function with different values
print(sort_words('without,hello,bag,world'))
