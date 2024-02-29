#Лабороторная работа №2: Князев Артём, Хапков Михаил, Позоян Рафаэль
def factorial(a): # функция факториала
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a - 1)
def placement_with_repetitions(n, k):
    print("Ответ:", n ** k)
#    print("Ответ:",factorial(n)//(factorial(k)*factorial(n-k)))

def placement_without_repetitions(n, k):
    print("Ответ:", int(factorial(n)/factorial(n-k)))
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
        print("Для создания n-значного пароля используются символы из алфавита {k1,k2,...k}.") # В условии задачи n = 4, а k = {+,*,A,!,2, 1}. Ответ = 4096

        print("Введите n")
        n = int(input())
        print("Введите k")
        k = int(input())

        placement_with_repetitions(n, k)

    elif choose == 4:
        print("В хоккейном турнире участвуют n команд. \n"
              "Разыгрываются золотые, серебряные и бронзовые медали. \n"
              "Сколькими способами могут быть распределены медали?") # В условии из учебника в турнире усаствуют 17 команд. Ответ = 4080
        print("")
        print("Введите n")
        n = int(input())
        print("Введите k")
        k = int(input())
        placement_without_repetitions(n, k)

if __name__ == '__main__':
    main()

