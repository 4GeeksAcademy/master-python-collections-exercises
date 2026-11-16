# `009` Todos los dígitos pares

## 📝 Instrucciones:

1. Completa la función `all_digits_even(start, end)`.

2. **Retorna** una lista con todos los números entre `start` y `end` (ambos incluidos) cuyos dígitos sean **todos** pares.

## 📎 Ejemplo:

```py
print(all_digits_even(2000, 2030))
# [2000, 2002, 2004, 2006, 2008, 2020, 2022, 2024, 2026, 2028]
```

## 💡 Pistas:

+ Convierte el número en string para recorrer sus dígitos uno a uno: `for digit in str(number)`.

+ La función incorporada `all()` retorna `True` si todos los valores de una colección son verdaderos.
