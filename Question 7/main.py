from base2 import base2
from base3 import base3
from base4 import base4
from base5 import base5
from base6 import base6
from base7 import base7
from base8 import base8
from base9 import base9
from base16 import base16

number = int(input('number: '))
base = input('base: ')
if base == '2':
    out = base2(number)
    print(out)
elif base == '3':
    out = base3(number)
    print(out)
elif base == '4':
    out = base4(number)
    print(out)
elif base == '5':
    out = base5(number)
    print(out)
elif base == '6':
    out = base6(number)
    print(out)
elif base == '7':
    out = base7(number)
    print(out)
elif base == '8':
    out = base8(number)
    print(out)
elif base == '9':
    out = base9(number)
    print(out)
elif base == '10':
    print(number)
elif base == '16':
    out = base16(number)
    print(out)