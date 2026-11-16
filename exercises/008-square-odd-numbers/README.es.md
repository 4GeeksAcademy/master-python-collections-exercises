# `008` Cuadrado de los impares

Un **list comprehension** construye una nueva lista en una sola línea, y puede filtrar valores con un `if`:

```py
numbers = [1, 2, 3, 4]
doubled_evens = [n * 2 for n in numbers if n % 2 == 0]  # [4, 8]
```

## 📝 Instrucciones:

1. Completa la función `square_odd_numbers(text)`. Recibe un string de enteros separados por comas.

2. **Retorna** una lista con el cuadrado de cada número **impar**, en el mismo orden.

## 📎 Ejemplo:

```py
print(square_odd_numbers("1,2,3,4,5,6,7,8,9"))  # [1, 9, 25, 49, 81]
```

## 💡 Pista:

+ Recuerda que `split()` te da strings: convierte cada uno con `int()` antes de calcular.
