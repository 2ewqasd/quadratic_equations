def data():
    print('Enter a, b and c')
    a = float(input())
    b = float(input())
    c = float(input())
    return a,b,c

def discriminant(a,b,c):
    d = (b ** 2) - (4 * a * c)
    return d

def first_case(a,b,d):
    'If D > 0'
    x1 = ((-1 * b) + (d ** 0.5)) / (2 * a)
    x2 = ((-1 * b) - (d ** 0.5)) / (2 * a)
    return x1,x2

def second_case(a,b):
    'If D = 0'
    x1 = x2 = -1 * (b / (2 * a))
    return x1,x2

def third_case():
    'If D < 0'
    x1 = x2 = 0
    print('No radix')

def fourth_case():
    'If b = 0 and c = 0'
    print('First radix = 0\nSecond radix = 0')

def fifth_case(a,c):
    'If b = 0 and c != 0'
    if (-1 * (c / a)) > 0:
        x1 = (-1 * (c / a)) ** 0.5
        x2 = -1 * ((-1 * (c / a)) ** 0.5)
    else:
        x1 = x2 = 0
        print('No radix')
    return x1,x2

def sixth_case(a,b):
    'If b != 0 and c = 0'
    x1 = 0
    x2 = -1 * (b / a)
    return x1,x2

def main():
    x1 = x2 = 0
    a,b,c = data()
    if b == 0 and c == 0:
        fourth_case()
    elif b == 0 and c != 0:
        x1,x2 = fifth_case(a,c)
    elif b != 0 and c == 0:
        x1,x2 = sixth_case(a,b)
    else:
        d = discriminant(a,b,c)
        if d > 0:
            x1,x2 = first_case(a,b,d)
        elif d == 0:
            x1,x2 = second_case(a,b)
        else:
            third_case()
    if x1 and x2 != 0:
        print(f'First radix = {x1}\nSecond radix = {x2}')
    
    

if __name__ == '__main__':
    main()