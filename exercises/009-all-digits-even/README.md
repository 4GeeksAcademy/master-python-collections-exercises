# `009` All Digits Even

## 📝 Instructions:

1. Complete the function `all_digits_even(start, end)`.

2. **Return** a list with every number between `start` and `end` (both included) whose digits are **all** even.

## 📎 Example:

```py
print(all_digits_even(2000, 2030))
# [2000, 2002, 2004, 2006, 2008, 2020, 2022, 2024, 2026, 2028]
```

## 💡 Hints:

+ Convert the number to a string to visit its digits one by one: `for digit in str(number)`.

+ The built-in function `all()` returns `True` if every value of a collection is true.
