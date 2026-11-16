# `018` Elementos en común

Los sets admiten operaciones matemáticas:

```py
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)  # {2, 3} intersection: in both
print(a | b)  # {1, 2, 3, 4} union: in any of them
print(a - b)  # {1} difference: in a but not in b
```

## 📝 Instrucciones:

1. Completa la función `common_elements(list_a, list_b)`.

2. **Retorna** una lista ordenada (sin duplicados) con los elementos que aparecen en **ambas** listas.

## 📎 Ejemplo:

```py
print(common_elements([5, 1, 3, 3, 8], [3, 8, 9, 5]))  # [3, 5, 8]
print(common_elements(["python", "java"], ["go", "rust"]))  # []
```

## 💡 Pista:

+ Convierte ambas listas con `set()`, usa `&` y ordena el resultado con `sorted()`.
