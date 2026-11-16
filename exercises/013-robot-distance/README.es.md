# `013` Distancia del robot

Un robot empieza en el punto `(0, 0)` y se mueve hacia arriba (`UP`), abajo (`DOWN`), izquierda (`LEFT`) y derecha (`RIGHT`). Sus movimientos se guardan en una lista:

```py
["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]
```

El número después de cada dirección es la cantidad de pasos.

## 📝 Instrucciones:

1. Completa la función `robot_distance(movements)`.

2. Calcula la posición final del robot.

3. **Retorna** la distancia en línea recta desde el punto de partida, redondeada al entero más cercano.

## 📎 Ejemplo:

```py
print(robot_distance(["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]))  # 2
```

## 💡 Pistas:

+ Usa dos variables `x` e `y`. `UP` suma a `y`, `DOWN` resta a `y`...

+ La distancia de `(0, 0)` a `(x, y)` es `math.sqrt(x ** 2 + y ** 2)`.
