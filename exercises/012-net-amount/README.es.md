# `012` Saldo neto

Una cuenta bancaria guarda un registro de transacciones en un solo string. Cada transacción es una letra seguida de una cantidad: `D` significa depósito y `W` significa retiro.

## 📝 Instrucciones:

1. Completa la función `net_amount(transactions)`.

2. **Retorna** el saldo final de la cuenta, empezando desde `0`.

## 📎 Ejemplo:

```py
print(net_amount("D 300 D 300 W 200 D 100"))  # 500
```

## 💡 Pistas:

+ Después de `split()`, la lista alterna tipo y cantidad: `['D', '300', 'D', '300', ...]`.

+ `range(0, len(parts), 2)` recorre las posiciones de dos en dos.
