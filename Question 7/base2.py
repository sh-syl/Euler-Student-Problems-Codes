def base2(n):
    m = '01'
    i = ''
    if n == 0:
        return '0'
    while n:
        mod = n % 2
        i = m[mod] + i
        n = n // 2
    return i

while __name__ == '__main__':
    n = int(input('Number: '))
    print(base2(n))