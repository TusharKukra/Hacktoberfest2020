import string
import math
def rangoli(size):
    alpha = list(string.ascii_lowercase)
    space = (size - 1) * 2
    print(alpha)
    dec = 0
    ii = 1
    for i in range(1, (size * 2)):
        count = 1
        index = size
        if i <= size:
            print('-' * ((size * 2 - 2) - dec), end='')
            for k in range(0, ii):
                if count == 1:
                    if k <= math.ceil(ii/2):
                        index = index - 1
                        print(alpha[index], end='')
                        count = 0
                    else:
                        index = index + 1
                        print(alpha[index], end='')
                        count = 0
                else:
                    count = 1
                    if k != (ii - 1):
                        print('-', end='')
            print('-' * ((size * 2 - 2) - dec), end='')
            if i < size:
                ii = ii + 4
                dec = dec + 2
        else:
            ii = ii - 4
            dec = dec - 2
            print('-' * ((size * 2 - 2) - dec), end='')
            for k in range(0, ii):
                if count == 1:
                    if k <= math.ceil(ii / 2):
                        index = index - 1
                        print(alpha[index], end='')
                        count = 0
                    else:
                        index = index + 1
                        print(alpha[index], end='')
                        count = 0
                else:
                    count = 1
                    if k != (ii - 1):
                        print('-', end='')
            print('-' * ((size * 2 - 2) - dec), end='')
        print()


size = int(input("Enter the Size:"))
rangoli(size)
