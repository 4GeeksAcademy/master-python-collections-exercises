# `016` Sort Records

Python compares tuples element by element: first the first element, and only if they are equal, the second one, and so on. That makes sorting by several criteria very easy.

## 📝 Instructions:

1. Complete the function `sort_records(records)`. It receives a list of strings with the format `"name,age,score"`.

2. Convert each record into a tuple `(name, age, score)` where all three values are strings.

3. **Return** the list of tuples sorted by name, then by age and then by score.

## 📎 Example:

```py
print(sort_records(["Tom,19,80", "John,20,90", "Jony,17,91", "Jony,17,93", "Jason,21,85"]))
# [('Jason', '21', '85'), ('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Tom', '19', '80')]
```

## 💡 Hints:

+ `tuple("Tom,19,80".split(","))` is `('Tom', '19', '80')`.

+ Because tuples are compared element by element, `sorted()` already applies the three criteria in order.
