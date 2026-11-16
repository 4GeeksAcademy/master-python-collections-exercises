def is_valid_password(password):
    return (
        6 <= len(password) <= 12
        and any(char.islower() for char in password)
        and any(char.isupper() for char in password)
        and any(char.isdigit() for char in password)
        and any(char in "$#@" for char in password)
    )


# Try your function with different values
print(is_valid_password('ABd1234@1'))
