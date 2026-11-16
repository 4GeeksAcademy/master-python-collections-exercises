# `014` Frecuencia de palabras

## 📝 Instrucciones:

1. Completa la función `word_frequency(text)`. Las palabras están separadas por espacios y los signos de puntuación forman parte de la palabra (`3?` y `3.` son palabras distintas).

2. **Retorna** un diccionario donde cada clave es una palabra y su valor es cuántas veces aparece.

3. Las claves deben estar insertadas en orden alfabético (como las ordena `sorted()`).

## 📎 Ejemplo:

```py
print(word_frequency("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."))
# {'2': 2, '3.': 1, '3?': 1, 'New': 1, 'Python': 5, 'Read': 1, 'and': 1, 'between': 1, 'choosing': 1, 'or': 2, 'to': 1}
```

Fíjate que `sorted()` pone primero los dígitos, luego las palabras en mayúscula y después las de minúscula.

## 💡 Pistas:

+ `counts.get(word, 0)` retorna `0` cuando la palabra aún no está en el diccionario.

+ Desde Python 3.7 los diccionarios mantienen el orden de inserción, así que puedes construir el resultado a partir de `sorted(counts)`.
