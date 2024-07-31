def base3(n):
    m = '012'
    i = ''
    if n == 0:
        return '0'
    while n:
        mod = n % 3
        i = m[mod] + i
        n = n // 3
    return i

while __name__ == '__main__':
    n = int(input('Number: '))
    print(base3(n))
