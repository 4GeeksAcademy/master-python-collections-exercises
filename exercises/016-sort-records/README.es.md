# `016` Ordenar registros

Python compara las tuplas elemento por elemento: primero el primer elemento y, solo si son iguales, el segundo, y así sucesivamente. Eso hace muy fácil ordenar con varios criterios.

## 📝 Instrucciones:

1. Completa la función `sort_records(records)`. Recibe una lista de strings con el formato `"name,age,score"`.

2. Convierte cada registro en una tupla `(name, age, score)` donde los tres valores son strings.

3. **Retorna** la lista de tuplas ordenada por nombre, luego por edad y luego por puntuación.

## 📎 Ejemplo:

```py
print(sort_records(["Tom,19,80", "John,20,90", "Jony,17,91", "Jony,17,93", "Jason,21,85"]))
# [('Jason', '21', '85'), ('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Tom', '19', '80')]
```

## 💡 Pistas:

+ `tuple("Tom,19,80".split(","))` es `('Tom', '19', '80')`.

+ Como las tuplas se comparan elemento por elemento, `sorted()` ya aplica los tres criterios en orden.
