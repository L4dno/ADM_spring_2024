#Лабороторная работа №2: Князев Артём, Хапков Михаил, Позоян Рафаэль
def fact(a): # функция факториала
    if a == 0:
        return 1
    elif a == 1:
        return 1
    elif a == 2:
        return 2
    else:
        return a*fact(a-1)

def combinations_rep(n:int, k:int): # сочетание с повторениями (n+k-1)!/k!*(n-1)!
    otv = fact(n+k-1)/(fact(k)*fact(n-1))
    print("Число равновозможных заказов равно:",int(otv))
    return 0

def combination(): # сочетание без повторений n!/(n-x)!
    pass 

def main():
    print("Выберите тему:")
    print("1 - Правило суммы")
    print("2 - Правило произведения")
    print("3 - Размещение с повторениями")
    print("4 - Размещение без повторений")
    print("5 - Сочетание с повторениями")
    print("6 - Сочетание без повторений")
    print("7 - Перестановка с повторениями")
    print("8 - Перестановка без повторений")
    print("0 - Закончить")

    choose = int(input())

    while choose != 0:
        if choose == 1:
            pass
        elif choose == 5:
            print("В кофейне представлено n видов напитков, молодой человек просит дать ему k любых напитков")
            n = int(input('введите n:'))
            k = int(input('введите k'))
            combinations_rep(n, k)
        elif choose == 6: 
            pass
        
        print("Выберите тему:")
        print("1 - Правило суммы")
        print("2 - Правило произведения")
        print("3 - Размещение с повторениями")
        print("4 - Размещение без повторений")
        print("5 - Сочетание с повторениями")
        print("6 - Сочетание без повторений")
        print("7 - Перестановка с повторениями")
        print("8 - Перестановка без повторений")
        print("0 - Закончить")

        choose = int(input())

    print('See u soon')


if __name__ == '__main__':
    main()





