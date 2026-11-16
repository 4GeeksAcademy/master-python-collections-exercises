# `015` Password Validator

A website only accepts passwords that meet **all** of these rules:

1. At least one lowercase letter (`a-z`).
2. At least one uppercase letter (`A-Z`).
3. At least one digit (`0-9`).
4. At least one of these symbols: `$`, `#` or `@`.
5. Between 6 and 12 characters long (both included).

## 📝 Instructions:

1. Complete the function `is_valid_password(password)`.

2. **Return** `True` if the password meets every rule and `False` otherwise.

## 📎 Example:

```py
print(is_valid_password("ABd1234@1"))  # True
print(is_valid_password("abc123"))  # False (no uppercase and no symbol)
```

## 💡 Hints:

+ `any(char.islower() for char in password)` tells you if at least one character is lowercase.

+ If you want to go further, you can solve it with regular expressions (`import re`).
