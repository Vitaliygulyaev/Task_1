def isPrime(a):
    count = f"{a} - простое число"
    for i in range(2, a):
        if (a % i == 0):
            count = f"{a} - непростое число"
            break
        else:
            continue
    print(count)

if __name__=="__main__":
    a = input("Введи число а: ")
    if type(a) is int:
        isPrime(a)
    elif type(a) is float:
        a = int(a)
        isPrime(a)
    elif type(a) is str:
        arr = []
        for i in a:
            if i.isdigit():
                arr.append(i)
        a = int(''.join(arr))
        isPrime(a)
    else:
        print("Некорректный ввод числа а...")


        
        

    

