# `005` Remove Duplicate Words

A **set** is a collection that can't contain repeated values. Converting a list to a set is the fastest way to remove duplicates.

## 📝 Instructions:

1. Complete the function `remove_duplicate_words(text)`. It receives a string of words separated by spaces.

2. **Return** a string with each word only once, sorted alphabetically and separated by spaces.

## 📎 Example:

```py
print(remove_duplicate_words("hello world and practice makes perfect and hello world again"))
# again and hello makes perfect practice world
```

## 💡 Hints:

+ `set(words)` removes the duplicates, but a set has no order.

+ `sorted()` accepts a set and returns a sorted list.
