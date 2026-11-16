# `003` Contar letras y dígitos

## 📝 Instrucciones:

1. Completa la función `count_letters_and_digits(text)`.

2. **Retorna** un diccionario con dos claves: `"letters"` (cuántas letras tiene el texto) y `"digits"` (cuántos dígitos). Los espacios y símbolos no se cuentan.

## 📎 Ejemplo:

```py
print(count_letters_and_digits("hello world! 123"))
# {'letters': 10, 'digits': 3}
```

## 💡 Pistas:

+ Un bucle `for` sobre un string recorre cada carácter.

+ `char.isalpha()` te dice si un carácter es una letra y `char.isdigit()` si es un dígito.
