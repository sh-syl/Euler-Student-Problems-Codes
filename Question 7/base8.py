def base8(n):
    m = '01234567'
    i = ''
    if n == 0:
        return '0'
    while n:
        mod = n % 8
        i = m[mod] + i
        n = n // 8
    return i

while __name__ == '__main__':
    n = int(input('Number: '))
    print(base8(n))