# `012` Net Amount

A bank account keeps a log of transactions in a single string. Each transaction is a letter followed by an amount: `D` means deposit and `W` means withdrawal.

## 📝 Instructions:

1. Complete the function `net_amount(transactions)`.

2. **Return** the final balance of the account, starting from `0`.

## 📎 Example:

```py
print(net_amount("D 300 D 300 W 200 D 100"))  # 500
```

## 💡 Hints:

+ After `split()`, the list alternates type and amount: `['D', '300', 'D', '300', ...]`.

+ `range(0, len(parts), 2)` visits every other position.
