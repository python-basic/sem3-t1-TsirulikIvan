def func(a,b):
    print('Multiplication a and b = : {}'.format(a * b))
    print('Addition a and b = : {}'.format(a + b))
    print('Divison a and b = : {}'.format(a / b))
    print('Subtraction a and b = : {}'.format(a - b))


if __name__ == '__main__':
    fn = float(input('Enter first number\n'))
    sn = float(input('Enter second number\n'))
    func(fn, sn)
