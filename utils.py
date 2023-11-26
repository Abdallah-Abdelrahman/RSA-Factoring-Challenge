
"""This module defines utils functions"""


def sum_digits(n):
    """Sum digits of a positive int ``n``"""
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

def is_prime(num):
    """Check if ``num`` is prime"""
    if num == 2:
        return True
    if (num % 2 == 0):
        return False
    if num > 9 and num % 5 == 0:
        return False
    if sum_digits(num) % 3 == 0:
        return False
    return False
