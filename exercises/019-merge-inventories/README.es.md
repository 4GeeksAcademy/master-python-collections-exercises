# `019` Unir inventarios

Dos tiendas guardan su stock en diccionarios donde cada clave es un producto y cada valor es la cantidad disponible.

## 📝 Instrucciones:

1. Completa la función `merge_inventories(store_a, store_b)`.

2. **Retorna** un **nuevo** diccionario con todos los productos de ambas tiendas. Si un producto está en las dos, suma las cantidades.

3. No modifiques los diccionarios originales.

## 📎 Ejemplo:

```py
store_a = {"apple": 5, "pear": 2}
store_b = {"apple": 3, "kiwi": 7}
print(merge_inventories(store_a, store_b))  # {'apple': 8, 'pear': 2, 'kiwi': 7}
print(store_a)  # {'apple': 5, 'pear': 2}
```

## 💡 Pistas:

+ `store_a.copy()` crea un nuevo diccionario, así no cambias el original.

+ `.items()` te permite recorrer las claves y los valores al mismo tiempo.
