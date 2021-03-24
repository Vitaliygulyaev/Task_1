def additional(a, i):
    rezult = a + i
    return rezult

def subtraction(a, i):
    rezult = a - i
    return rezult

def multiplication(a, i):
    rezult = a * i
    return rezult

def division(a, i):
    rezult = a / i
    return rezult

def exponentiation(a, i):
    rezult = a ** i
    return rezult

def integer_division(a, i):
    rezult = a // i
    return rezult

def remainder_division(a, i):
    rezult = a % i
    return rezult

def proverka(c):
    c = list(c)
    check_digit = False
    check_symbol = False
    for i in range(len(c)):
        if c[i].isdigit():
            check_digit = True
            i = len(c)
    for i in range(len(c)):
        if c[i] == "+" or c[i] == "-" or c[i] == "*" or c[i] == "/" or c[i] == "**" or c[i] == "%" :
            check_symbol = True
            i = len(c)
    if (check_digit is True) and (check_symbol is True):
        c = "".join(c)
        c, e = parse(c)
        return c, e
    elif (check_digit is True) and (check_symbol is False):
        c = "".join(c) + "+"
        c, e = parse(c)
        return c, e
    elif (check_digit is False) and (check_symbol is True):
        b = str(ord(c[0]))
        c = "".join(c) + b
        c, e = parse(c)
        print("""Вы ввели строку не содержащую хотя бы одну цифру...
                    Вывод в соответствие с кодом ASCII: """+str(b))
        return c, e
    elif (check_digit is False) and (check_symbol is False):
        b = str(ord(c[0]))
        print("""Вы ввели строку не содержащую хотя бы одну цифру...
                    Вывод в соответствие с кодом ASCII: """+str(b))
        c = "".join(c) + b + "+"
        c, e = parse(c)
        return c, e

def parse(b):
    c = []
    e = []
    for i in b:
        if i.isdigit() or i == "." or i == ",":
            if i == ",":
                i = "."
            c.append(i)
        elif i == "+" or i == "-" or i == "*" or i == "/" or i == "%" :
            e.append(i)
    return c, e

def get_operation(e):
    operation = ""
    if len(e) > 1:
        if e[0] == "/" and e[1] == "/":
            operation = "//"
            return operation
        elif e[0] == "*" and e[1] == "*":
            operation = "**"
            return operation
        else:
            operation = e[0]
            return operation
    else:
        operation = e[0]
        return operation




def get_number(c):
    c = "".join(c)
    if c.count(".") == 1:
        c = float(c)
        return c
    elif c.count(".") > 1:
        count = True
        d = []
        for i in c:
            if (count is True and i == ".") or (i.isdigit()):
                d.append(i)
                if (d.count(".") == 1):
                     count = False
        c = float("".join(d))
        return c
    else:
        c = int(c)
        return c
            
def proverka_a(a):
    a = list(a)
    check_digit = False
    check_symbol = False
    for i in range(len(a)):
        if a[i].isdigit():
            check_digit = True
            i = len(a)
    for i in range(len(a)):
        if a[i] == "+" or a[i] == "-" or a[i] == "*" or a[i] == "/" or a[i] == "**" or a[i] == "//" or a[i] == "%" :
            check_symbol = True
            i = len(a)
    if (check_digit is True) and (check_symbol is True):
        a = "".join(a)
        rez = parse(a)
        a = rez[0]
        a = get_number(a)
        return a
    elif (check_digit is True) and (check_symbol is False):
        a = "".join(a)
        rez = parse(a)
        a = rez[0]
        a = get_number(a)
        return a
    elif (check_digit is False) and (check_symbol is True):
        b = ord(a[0])
        print("""Вы ввели строку не содержащую хотя бы одну цифру...
                    Вывод в соответствие с кодом ASCII: """+str(b))
        return b
    elif (check_digit is False) and (check_symbol is False):
        b = ord(a[0])
        print("""Вы ввели строку не содержащую хотя бы одну цифру...
                    Вывод в соответствие с кодом ASCII: """+str(b))
        return b    


if __name__=="__main__":
    a = input("Введите число: ")
    while a == "":
        a = input("Пустая строка? ДА ТЫ РОФЛИШЬ!!! Введи число: ")
    a = proverka_a(a)
    start = True
    while start == True:
        b = input("Введите знак операции и число (например: + 2): ")
        while b == "":
            b = input("Пустая строка? ДА ТЫ РОФЛИШЬ!! Введи знак операции и число (например: + 2): ")
        if b.count("=") < 1:
            c, e = proverka(b)
            print(c)
            print(e)
            c = get_number(c)
            operation = get_operation(e)
            print(str(c))
            print(operation)
            print(str(a))
            if operation == "+":
                a = additional(a, c)
            elif operation == "-":
                a = subtraction(a, c)
            elif operation == "*":
                a = multiplication(a, c)
            elif operation == "/":
                if c != 0:
                    a = division(a, c)
                else:
                    c, e = proverka(b)
                    c = get_number(c)
                    operation = get_operation(e)
            elif operation == "**":
                a = exponentiation(a, c)
            elif operation == "//":
                if c != 0:
                    a = integer_division(a, c)
                else:
                    c, e = proverka(b)
                    c = get_number(c)
                    operation = get_operation(e)
            elif operation == "%":
                if c != 0:
                    a = remainder_division(a, c)
                else:
                    c, e = proverka(b)
                    c = get_number(c)
                    operation = get_operation(e)
            print("Результат: "+str(a))
        else:
            print("Итого: "+str(a))
            start = False


