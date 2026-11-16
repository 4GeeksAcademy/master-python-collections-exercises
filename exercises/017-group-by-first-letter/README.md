# `017` Group by First Letter

Dictionaries can store any value, including lists. A very common pattern is to **group** items under a key.

## 📝 Instructions:

1. Complete the function `group_by_first_letter(words)`. It receives a list of lowercase words.

2. **Return** a dictionary where each key is a first letter and its value is the list of words that start with that letter, in their original order.

## 📎 Example:

```py
print(group_by_first_letter(["apple", "banana", "avocado", "blueberry", "cherry"]))
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

## 💡 Hints:

+ `word[0]` is the first letter of a word.

+ If the letter is not in the dictionary yet, create an empty list for it before appending.
