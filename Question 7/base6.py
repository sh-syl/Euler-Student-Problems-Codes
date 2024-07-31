def base6(n):
    m = '012345'
    i = ''
    if n == 0:
        return '0'
    while n:
        mod = n % 6
        i = m[mod] + i
        n = n // 6
    return i

while __name__ == '__main__':
    n = int(input('Number: '))
    print(base6(n))