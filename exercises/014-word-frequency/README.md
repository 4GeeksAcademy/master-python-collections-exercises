# `014` Word Frequency

## 📝 Instructions:

1. Complete the function `word_frequency(text)`. Words are separated by spaces and punctuation stays attached to the word (`3?` and `3.` are different words).

2. **Return** a dictionary where each key is a word and its value is how many times it appears.

3. The keys must be inserted in alphabetical order (as `sorted()` orders them).

## 📎 Example:

```py
print(word_frequency("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."))
# {'2': 2, '3.': 1, '3?': 1, 'New': 1, 'Python': 5, 'Read': 1, 'and': 1, 'between': 1, 'choosing': 1, 'or': 2, 'to': 1}
```

Notice that `sorted()` puts digits first, then uppercase words and then lowercase words.

## 💡 Hints:

+ `counts.get(word, 0)` returns `0` when the word is not in the dictionary yet.

+ Since Python 3.7 dictionaries keep the insertion order, so you can build the result from `sorted(counts)`.
