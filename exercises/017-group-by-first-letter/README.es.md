# `017` Agrupar por primera letra

Los diccionarios pueden guardar cualquier valor, incluso listas. Un patrón muy común es **agrupar** elementos bajo una clave.

## 📝 Instrucciones:

1. Completa la función `group_by_first_letter(words)`. Recibe una lista de palabras en minúscula.

2. **Retorna** un diccionario donde cada clave es una primera letra y su valor es la lista de palabras que empiezan con esa letra, en su orden original.

## 📎 Ejemplo:

```py
print(group_by_first_letter(["apple", "banana", "avocado", "blueberry", "cherry"]))
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

## 💡 Pistas:

+ `word[0]` es la primera letra de una palabra.

+ Si la letra todavía no está en el diccionario, crea una lista vacía para ella antes de añadir.
