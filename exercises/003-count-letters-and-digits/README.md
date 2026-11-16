# `003` Count Letters and Digits

## 📝 Instructions:

1. Complete the function `count_letters_and_digits(text)`.

2. **Return** a dictionary with two keys: `"letters"` (how many letters the text has) and `"digits"` (how many digits). Spaces and symbols are not counted.

## 📎 Example:

```py
print(count_letters_and_digits("hello world! 123"))
# {'letters': 10, 'digits': 3}
```

## 💡 Hints:

+ A `for` loop over a string visits each character.

+ `char.isalpha()` tells you if a character is a letter and `char.isdigit()` if it's a digit.
