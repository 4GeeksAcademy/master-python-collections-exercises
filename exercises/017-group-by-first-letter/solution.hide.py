def group_by_first_letter(words):
    groups = {}
    for word in words:
        letter = word[0]
        if letter not in groups:
            groups[letter] = []
        groups[letter].append(word)
    return groups


# Try your function with different values
print(group_by_first_letter(['apple', 'banana', 'avocado', 'blueberry', 'cherry']))
