def base16(n):
    m = '0123456789abcdef'
    i = ''
    if n == 0:
        return '0'
    while n:
        mod = n % 16
        i = m[mod] + i
        n = n // 16
    return i

while __name__ == '__main__':
    n = int(input('Number: '))
    print(base16(n))