def largest_prime_factor(number: int) -> int:
    factor = 2
    while factor * factor <= number:
        if number % factor:
            factor += 1
        else:
            number //= factor
    return number


print(largest_prime_factor(600_851_475_143))
