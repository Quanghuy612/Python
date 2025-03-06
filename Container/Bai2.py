def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = tuple(n for n in range(1, 51) if is_prime(n))

print("Danh sách số nguyên tố từ 1 đến 50:", prime_numbers)
