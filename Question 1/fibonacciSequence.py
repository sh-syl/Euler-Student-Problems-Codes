def create():
    num1 = 0
    num2 = 1
    result = []
    while num2 < 1000:
        result.append(num2)
        num2 += num1
        num1 = num2
    print(result)

create()