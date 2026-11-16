# `002` Sort Words

## 📝 Instructions:

1. Complete the function `sort_words(text)`. It receives a string of words separated by commas, without spaces.

2. **Return** a string with the same words sorted alphabetically, also separated by commas.

## 📎 Example:

```py
print(sort_words("without,hello,bag,world"))  # bag,hello,without,world
```

## 💡 Hints:

+ `text.split(",")` converts the string into a list of words.

+ `sorted()` returns a new sorted list and `",".join(words)` joins a list back into a string.
