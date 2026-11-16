# `019` Merge Inventories

Two stores keep their stock in dictionaries where each key is a product and each value is the quantity available.

## 📝 Instructions:

1. Complete the function `merge_inventories(store_a, store_b)`.

2. **Return** a **new** dictionary with every product of both stores. If a product is in both, add up the quantities.

3. Don't modify the original dictionaries.

## 📎 Example:

```py
store_a = {"apple": 5, "pear": 2}
store_b = {"apple": 3, "kiwi": 7}
print(merge_inventories(store_a, store_b))  # {'apple': 8, 'pear': 2, 'kiwi': 7}
print(store_a)  # {'apple': 5, 'pear': 2}
```

## 💡 Hints:

+ `store_a.copy()` creates a new dictionary, so you don't change the original one.

+ `.items()` lets you loop over the keys and values at the same time.
