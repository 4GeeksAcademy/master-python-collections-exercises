# `010` Binary Numbers Divisible by 5

`int()` can convert a binary string into a decimal number if you pass the base as the second argument:

```py
print(int("0101", 2))  # 5
```

## 📝 Instructions:

1. Complete the function `binary_divisible_by_five(text)`. It receives a string of 4-digit binary numbers separated by commas.

2. **Return** a list with the binary numbers (as strings, in the same order) whose decimal value is divisible by `5`.

## 📎 Example:

```py
print(binary_divisible_by_five("0100,0011,1010,1001"))  # ['1010']
```

## 💡 Hint:

+ Keep the original string in the result; use `int(binary, 2)` only to check the condition.
