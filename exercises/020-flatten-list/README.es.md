# `020` Aplanar una lista

## 📝 Instrucciones:

1. Completa la función `flatten(nested)`. Recibe una lista de listas de números.

2. **Retorna** una sola lista con todos los números, en el mismo orden.

3. Luego, como extra, escribe la misma lógica con un list comprehension.

## 📎 Ejemplo:

```py
print(flatten([[1, 2], [3], [], [4, 5, 6]]))  # [1, 2, 3, 4, 5, 6]
```

## 💡 Pistas:

+ Con bucles: recorre cada lista interna y añade sus valores al resultado con `append()` (o `extend()`).

+ Con un comprehension: `[value for row in nested for value in row]`.
