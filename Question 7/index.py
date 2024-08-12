def baseTest(n):
    m = '0123456789abcdefghijklmnopqrstuvwxyz'
    i = ''
    if n == 0:
        return '0'
    while n:
        mod = n % base
        i = m[mod] + i
        n = n // base
    return i

while __name__ == '__main__':
    base = int(input('Base: '))
    n = int(input('Number: '))
    print(baseTest(n))
