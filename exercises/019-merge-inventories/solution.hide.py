def merge_inventories(store_a, store_b):
    merged = store_a.copy()
    for product, quantity in store_b.items():
        merged[product] = merged.get(product, 0) + quantity
    return merged


# Try your function with different values
print({"apple": 5, "pear": 2}, {"apple": 3, "kiwi": 7})
