# `015` Validador de contraseñas

Un sitio web solo acepta contraseñas que cumplan **todas** estas reglas:

1. Al menos una letra minúscula (`a-z`).
2. Al menos una letra mayúscula (`A-Z`).
3. Al menos un dígito (`0-9`).
4. Al menos uno de estos símbolos: `$`, `#` o `@`.
5. Entre 6 y 12 caracteres de longitud (ambos incluidos).

## 📝 Instrucciones:

1. Completa la función `is_valid_password(password)`.

2. **Retorna** `True` si la contraseña cumple todas las reglas y `False` en caso contrario.

## 📎 Ejemplo:

```py
print(is_valid_password("ABd1234@1"))  # True
print(is_valid_password("abc123"))  # False (no uppercase and no symbol)
```

## 💡 Pistas:

+ `any(char.islower() for char in password)` te dice si al menos un carácter es minúscula.

+ Si quieres ir más allá, puedes resolverlo con expresiones regulares (`import re`).
