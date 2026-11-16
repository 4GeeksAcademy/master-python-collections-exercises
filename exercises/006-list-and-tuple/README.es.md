# `006` Lista y tupla

Usando `*args` en los parámetros, una función puede recibir **cualquier cantidad de argumentos**. Dentro de la función, `args` es una tupla con todos ellos:

```py
def show(*args):
    print(args)

show(1, 2, 3)  # (1, 2, 3)
```

## 📝 Instrucciones:

1. Completa la función `list_and_tuple(*numbers)`. Recibe cualquier cantidad de enteros.

2. Convierte cada número en string.

3. **Retorna** dos valores: una **lista** y una **tupla**, ambas con los números como strings.

## 📎 Ejemplo:

```py
print(list_and_tuple(34, 67, 55))
# (['34', '67', '55'], ('34', '67', '55'))
```

## 💡 Pista:

+ `list()` y `tuple()` convierten cualquier colección en una lista o en una tupla.
