def base7(n):
    m = '0123456'
    i = ''
    if n == 0:
        return '0'
    while n:
        mod = n % 7
        i = m[mod] + i
        n = n // 7
    return i

while __name__ == '__main__':
    n = int(input('Number: '))
    print(base7(n))