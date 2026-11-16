def net_amount(transactions):
    parts = transactions.split()
    balance = 0
    for i in range(0, len(parts), 2):
        amount = int(parts[i + 1])
        if parts[i] == "D":
            balance += amount
        elif parts[i] == "W":
            balance -= amount
    return balance


# Try your function with different values
print(net_amount('D 300 D 300 W 200 D 100'))
