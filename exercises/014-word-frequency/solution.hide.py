def word_frequency(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return {word: counts[word] for word in sorted(counts)}


# Try your function with different values
print(word_frequency('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'))
