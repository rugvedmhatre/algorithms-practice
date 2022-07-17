def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_fast(n):
    fib_last_digits = [0, 1]

    for i in range(2, n+1):
        fib_last_digits.append((fib_last_digits[i-1] + fib_last_digits[i-2]) % 10)

    return fib_last_digits[n]

n = int(input())
print(get_fibonacci_last_digit_fast(n))
