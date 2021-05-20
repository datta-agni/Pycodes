# A python program to create a basic calculator.
print("    Choose the operator\n""1.Addition\t""2.Subtraction\t""3.Multiplication\t""4.Division\t""5.Exponents")
ch = int(input("    Enter your choice:    "))
a = float(input('Enter the first number:    '))
b = float(input('Enter the second number:   '))


def operator(ch):
    switcher = {
        1: add(a, b),
        2: sub(a, b),
        3: mul(a, b),
        4: div(a, b),
        5: exp(a, b),
    }
    func = switcher.get(ch)
    print("\n", "    Your Answer is:    ", func)


def add(a, b):
    c = a + b
    # print(c)
    return c


def sub(a, b):
    c = a - b
    # print(c)
    return c


def div(a, b):
    c = a / b
    # print(c)
    return c


def mul(a, b):
    c = a * b
    # print(c)
    return c


def exp(a, b):
    c = a ** b
    # print(c)
    return c


operator(ch)
