def sieve_of_eratosthenes(n):
    # Создаем список истинных значений, которые будут отмечать, является ли число простым
    primes = [True for _ in range(n+1)]
    p = 2  # Начинаем с первого простого числа

    while (p * p <= n):  # Проверяем до корня из n
        if primes[p]:  # Если число еще не было вычеркнуто, оно простое
            # Вычеркиваем все кратные p, начиная с p^2
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    # Собираем и выводим все простые числа
    prime_numbers = [p for p in range(2, n+1) if primes[p]]
    return prime_numbers

# Вводим натуральное число
n = int(input("Введите число N: "))

# Нахождение всех простых чисел до N
prime_numbers = sieve_of_eratosthenes(n)

# Выводим результат
print(f"Простые числа до {n}: {prime_numbers}")
