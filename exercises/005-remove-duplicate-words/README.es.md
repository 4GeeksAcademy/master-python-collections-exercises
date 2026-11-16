# `005` Eliminar palabras duplicadas

Un **set** (conjunto) es una colección que no puede contener valores repetidos. Convertir una lista en set es la forma más rápida de eliminar duplicados.

## 📝 Instrucciones:

1. Completa la función `remove_duplicate_words(text)`. Recibe un string de palabras separadas por espacios.

2. **Retorna** un string con cada palabra una sola vez, ordenadas alfabéticamente y separadas por espacios.

## 📎 Ejemplo:

```py
print(remove_duplicate_words("hello world and practice makes perfect and hello world again"))
# again and hello makes perfect practice world
```

## 💡 Pistas:

+ `set(words)` elimina los duplicados, pero un set no tiene orden.

+ `sorted()` acepta un set y retorna una lista ordenada.
