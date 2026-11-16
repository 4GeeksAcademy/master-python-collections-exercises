# `018` Common Elements

Sets support mathematical operations:

```py
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)  # {2, 3} intersection: in both
print(a | b)  # {1, 2, 3, 4} union: in any of them
print(a - b)  # {1} difference: in a but not in b
```

## 📝 Instructions:

1. Complete the function `common_elements(list_a, list_b)`.

2. **Return** a sorted list (without duplicates) with the elements that appear in **both** lists.

## 📎 Example:

```py
print(common_elements([5, 1, 3, 3, 8], [3, 8, 9, 5]))  # [3, 5, 8]
print(common_elements(["python", "java"], ["go", "rust"]))  # []
```

## 💡 Hint:

+ Convert both lists with `set()`, use `&` and sort the result with `sorted()`.
