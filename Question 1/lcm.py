def lcm(x,y):
    a = x
    b = y
    while y:
        x,y = y,x % y
    return a * b // x

while True:
    num = input('Numbers(Separate by space): ').split()
    LCM = int(num[0])
    for i in range(len(num)):
        if i+1 == len(num):
            break
        LCM = lcm(LCM,int(num[i+1]))
    print(LCM)
    