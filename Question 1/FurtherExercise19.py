import random as ran

a = 112
b = 189
c = 144

# Bei's turn
if a > c:
    b -= c
elif c < a:
    b -= a
else:
    if ran.randint(0, 1) == 0:
        b -= c
    else:
        b -= a
# Arjan's turn
if b > c:
    a -= c
elif c < b:
    a -= b
else:
    if ran.randint(0, 1) == 0:
        a -= c
    else:
        a -= b
# Chloe's turn
if b > a:
    c -= a
elif b < a:
    c -= b
else:
    if ran.randint(0, 1) == 0:
        c -= a
    else:
        c -= b


print(a,b,c)