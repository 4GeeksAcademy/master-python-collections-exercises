def remove_duplicate_words(text):
    return " ".join(sorted(set(text.split())))


# Try your function with different values
print(remove_duplicate_words('hello world and practice makes perfect and hello world again'))
