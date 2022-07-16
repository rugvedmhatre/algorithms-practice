def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_fast(a, b):
    remainder = a % b
    if remainder <= 0:
        return b
    else:
        return gcd_fast(b , remainder)

a, b = map(int, input().split())
print(gcd_fast(a, b))
