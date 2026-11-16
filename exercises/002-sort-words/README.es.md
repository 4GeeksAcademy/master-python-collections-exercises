# `002` Ordenar palabras

## 📝 Instrucciones:

1. Completa la función `sort_words(text)`. Recibe un string de palabras separadas por comas, sin espacios.

2. **Retorna** un string con las mismas palabras ordenadas alfabéticamente, también separadas por comas.

## 📎 Ejemplo:

```py
print(sort_words("without,hello,bag,world"))  # bag,hello,without,world
```

## 💡 Pistas:

+ `text.split(",")` convierte el string en una lista de palabras.

+ `sorted()` retorna una nueva lista ordenada y `",".join(words)` vuelve a unir una lista en un string.
