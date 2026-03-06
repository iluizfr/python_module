import time
from typing import Generator


def fibonacci(index: int) -> int:
    if index < 0:
        return -1
    if index == 0:
        return 0
    if index == 1:
        return 1
    return (fibonacci(index - 1) + fibonacci(index - 2))


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

