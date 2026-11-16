# `008` Square Odd Numbers

A **list comprehension** builds a new list in a single line, and it can filter values with an `if`:

```py
numbers = [1, 2, 3, 4]
doubled_evens = [n * 2 for n in numbers if n % 2 == 0]  # [4, 8]
```

## 📝 Instructions:

1. Complete the function `square_odd_numbers(text)`. It receives a string of integers separated by commas.

2. **Return** a list with the square of each **odd** number, in the same order.

## 📎 Example:

```py
print(square_odd_numbers("1,2,3,4,5,6,7,8,9"))  # [1, 9, 25, 49, 81]
```

## 💡 Hint:

+ Remember that `split()` gives you strings: convert each one with `int()` before calculating.
