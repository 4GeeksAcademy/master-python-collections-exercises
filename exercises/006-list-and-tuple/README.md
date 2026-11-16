# `006` List and Tuple

Using `*args` in the parameters, a function can receive **any number of arguments**. Inside the function, `args` is a tuple with all of them:

```py
def show(*args):
    print(args)

show(1, 2, 3)  # (1, 2, 3)
```

## 📝 Instructions:

1. Complete the function `list_and_tuple(*numbers)`. It receives any number of integers.

2. Convert each number to a string.

3. **Return** two values: a **list** and a **tuple**, both with the numbers as strings.

## 📎 Example:

```py
print(list_and_tuple(34, 67, 55))
# (['34', '67', '55'], ('34', '67', '55'))
```

## 💡 Hint:

+ `list()` and `tuple()` convert any collection into a list or a tuple.
