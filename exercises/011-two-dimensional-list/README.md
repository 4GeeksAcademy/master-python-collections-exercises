# `011` Two-Dimensional List

A two-dimensional list (or **matrix**) is a list of lists. `matrix[i][j]` is the value in row `i` and column `j`.

## 📝 Instructions:

1. Complete the function `two_dimensional_list(rows, columns)`.

2. **Return** a matrix with `rows` rows and `columns` columns, where the value in row `i` and column `j` is `i * j`.

## 📎 Example:

```py
print(two_dimensional_list(3, 5))
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
```

## 💡 Hint:

+ Use two nested loops: the outer one builds each row and the inner one fills its columns.
