#Лабороторная работа №2: Князев Артём, Хапков Михаил, Позоян Рафаэль
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def placement_with_repetitions(m, n):
    print(m ** n)

def placement_without_repetitions(n, k):
    print(int(factorial(n)/factorial(n-k)))
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

    if choose == 3:
        print("Введите m")
        m = int(input())
        print("Введите n")
        n = int(input())

        if n > m:
            placement_with_repetitions(m, n)
        else:
            print("Неправильный ввод данных (m<=n)")

    elif choose == 4:
        print("Введите n")
        n = int(input()) 
        print("Введите k")
        k = int(input())

        placement_without_repetitions(n, k)

if __name__ == '__main__':
    main()

