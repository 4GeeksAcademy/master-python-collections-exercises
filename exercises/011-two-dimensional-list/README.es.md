# `011` Lista bidimensional

Una lista bidimensional (o **matriz**) es una lista de listas. `matrix[i][j]` es el valor de la fila `i` y la columna `j`.

## 📝 Instrucciones:

1. Completa la función `two_dimensional_list(rows, columns)`.

2. **Retorna** una matriz de `rows` filas y `columns` columnas, donde el valor de la fila `i` y la columna `j` sea `i * j`.

## 📎 Ejemplo:

```py
print(two_dimensional_list(3, 5))
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
```

## 💡 Pista:

+ Usa dos bucles anidados: el exterior construye cada fila y el interior llena sus columnas.
