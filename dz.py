def data():
    a,b,c = map(float, input().split())
    return a,b,c

def decision(a,b,c):
    x1 = x2 = 0
    d = (b ** 2) - (4 * a * c)
    if b == 0 and c == 0:
        print('First radix = 0\nSecond radix = 0')
    elif b == 0 and c != 0:
        if (-1 * (c / a)) > 0:
            x1 = (-1 * (c / a)) ** 0.5
            x2 = -1 * ((-1 * (c / a)) ** 0.5)
        else:
            x1 = x2 = 0
            print('No radix')
    elif b != 0 and c == 0:
        x1 = 0
        x2 = -1 * (b / a)
    else:
        if d > 0:
            x1 = ((-1 * b) + (d ** 0.5)) / (2 * a)
            x2 = ((-1 * b) - (d ** 0.5)) / (2 * a)
        elif d == 0:
            x1 = x2 = -1 * (b / (2 * a))
        else:
            x1 = x2 = 0
            print('No radix')
    if x1 and x2 != 0:
        print(f'First radix = {x1}\nSecond radix = {x2}')
    return x1,x2

def main():
    a,b,c = data()
    x1,x2 = decision(a,b,c)

if __name__ == '__main__':
    main()