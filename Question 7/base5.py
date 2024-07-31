def base5(n):
    m = '01234'
    i = ''
    if n == 0:
        return '0'
    while n:
        mod = n % 4
        i = m[mod] + i
        n = n // 4
    return i

while __name__ == '__main__':
    n = int(input('Number: '))
    print(base5(n))