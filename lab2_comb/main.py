#Лабороторная работа №2: Князев Артём, Хапков Михаил, Позоян Рафаэль
def fact(a): # функция факториала
    if a == 0 or a == 1:
        return 1
    else:
        return a * fact(a - 1)

def combinations_with_repetitions(n:int, k:int): # сочетание с повторениями (n+k-1)!/k!*(n-1)!
    otv = fact(n+k-1)/(fact(k)*fact(n-1))
    print("Число равновозможных заказов равно: ",int(otv), '\n')

def combination_without_repetitions(n:int, k:int): # сочетание без повторений n!/(n-x)!
    otv = fact(n)/(fact(n-k)*fact(k))
    print("количество способов: ", int(otv), '\n')

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
            print("n ребят собрали в саду k яблока. Сколькими способами они могут их разделить между собой?") # в задаче из учебника n = 3, k=63, C=2080
            n = int(input('введите n: '))
            k = int(input('введите k: '))
            combinations_with_repetitions(n, k)
        elif choose == 6: 
            print("У вас есть n различных книг, и вы хотите выбрать k книги для чтения. Сколькими способами вы можете выбрать эти книги?") # в задаче n=5, k=3, C=10
            n = int(input('введите n: '))
            k = int(input('введите k: '))
            combination_without_repetitions(n, k)

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





