def factorize(n):
    factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    result = sorted(factors)  # Useless
    return result


for i in range(101):
    print(i, ':', factorize(i))
