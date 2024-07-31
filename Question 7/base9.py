def base9(n):
    m = '012345678'
    i = ''
    if n == 0:
        return '0'
    while n:
        mod = n % 9
        i = m[mod] + i
        n = n // 9
    return i

while __name__ == '__main__':
    n = int(input('Number: '))
    print(base9(n))