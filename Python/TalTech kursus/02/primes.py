"""Primes identifier."""
import math

def is_prime_number(number: int) -> bool:
    """
    Check if number (given in function parameter) is prime.

    If number is prime -> return True
    If number is not prime -> return False

    :param number: number for check.
    :return: boolean True if number is prime or False if number is not prime.
    """
    if number == 1 or number == 0:  # prime nums are greater than 1
        return False
    if number % 2 == 0 and number > 2:  # return false if doesn't fit
        return False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))