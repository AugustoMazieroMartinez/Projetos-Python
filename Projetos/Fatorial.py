"""
Function to calculate the factorial of a given number.

Args:
    n (int): The number for which the factorial is to be calculated. Must be a non-negative integer.

Returns:
    int: The factorial of the given number.

Raises:
    ValueError: If the input is a negative integer.

Example:
    >>> factorial(5)
    120
"""
value = int(input('Digite um número: '))

# def factorial(value):
#     if value < 0:
#         raise ValueError('O valor deve ser positivo')
#     if value == 0:
#         return 1   
#     return value * factorial(value - 1)
# print(factorial(value))

def factorial(value):
    if value == 0:
        return 1
    elif value < 0:
        return 'O valor deve ser positivo'
    elif value > 0:
        return value * factorial(value - 1)
print(factorial(value))