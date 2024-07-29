def factorize(n):
    factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    return factors

while __name__ == "__main__":
    print(factorize(int(input('Number: '))))
