# `013` Robot Distance

A robot starts at point `(0, 0)` and moves `UP`, `DOWN`, `LEFT` and `RIGHT`. Its movements are stored in a list:

```py
["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]
```

The number after each direction is the number of steps.

## 📝 Instructions:

1. Complete the function `robot_distance(movements)`.

2. Calculate the final position of the robot.

3. **Return** the straight-line distance from the starting point, rounded to the nearest integer.

## 📎 Example:

```py
print(robot_distance(["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]))  # 2
```

## 💡 Hints:

+ Keep two variables `x` and `y`. `UP` adds to `y`, `DOWN` subtracts from `y`...

+ The distance from `(0, 0)` to `(x, y)` is `math.sqrt(x ** 2 + y ** 2)`.
