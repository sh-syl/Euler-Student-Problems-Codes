def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


while True:
    num = input('Numbers(Separate by space): ').split()
    GCD = int(num[0])
    for i in range(len(num)):
        if i + 1 == len(num):
            break
        GCD = gcd(GCD, int(num[i + 1]))
    print(GCD)
