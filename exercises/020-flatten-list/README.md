# `020` Flatten a List

## 📝 Instructions:

1. Complete the function `flatten(nested)`. It receives a list of lists of numbers.

2. **Return** a single list with all the numbers, in the same order.

3. Then, as a bonus, write the same logic with a list comprehension.

## 📎 Example:

```py
print(flatten([[1, 2], [3], [], [4, 5, 6]]))  # [1, 2, 3, 4, 5, 6]
```

## 💡 Hints:

+ With loops: go through each inner list and `append()` (or `extend()`) its values to the result.

+ With a comprehension: `[value for row in nested for value in row]`.
