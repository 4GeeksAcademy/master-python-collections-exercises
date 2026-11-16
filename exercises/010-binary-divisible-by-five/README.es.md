# `010` Binarios divisibles entre 5

`int()` puede convertir un string binario en un número decimal si le pasas la base como segundo argumento:

```py
print(int("0101", 2))  # 5
```

## 📝 Instrucciones:

1. Completa la función `binary_divisible_by_five(text)`. Recibe un string de números binarios de 4 dígitos separados por comas.

2. **Retorna** una lista con los números binarios (como strings, en el mismo orden) cuyo valor decimal sea divisible entre `5`.

## 📎 Ejemplo:

```py
print(binary_divisible_by_five("0100,0011,1010,1001"))  # ['1010']
```

## 💡 Pista:

+ Guarda el string original en el resultado; usa `int(binary, 2)` solo para comprobar la condición.
