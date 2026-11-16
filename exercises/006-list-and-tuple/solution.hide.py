def list_and_tuple(*numbers):
    texts = [str(number) for number in numbers]
    return texts, tuple(texts)


# Try your function with different values
print(list_and_tuple(34, 67, 55))
