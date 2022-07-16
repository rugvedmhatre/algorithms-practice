def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_fast(a, b):
    remainder = a % b
    if remainder <= 0:
        return b
    else:
        return gcd_fast(b , remainder)

def lcm_fast(a, b):
    gcd = gcd_fast(a, b)
    return ( a * b ) // gcd

a, b = map(int, input().split())
print(lcm_fast(a, b))

