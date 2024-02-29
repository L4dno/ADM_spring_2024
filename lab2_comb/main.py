#Лабороторная работа №2: Князев Артём, Хапков Михаил, Позоян Рафаэль

# функция факториала
def fact(a:int): 
    if a == 0 or a == 1:
        return 1
    else:
        return a * fact(a - 1)
    
# вычисление перестановок с повторениями
# где a - массив длины n с количеством
# разных элементов
def perm_reps(n:int, a:int):
    tmp = 1
    for item in a:
        tmp *= fact(item)
    return int(fact(n)/tmp)

#вычисление сочетаний без повторений
def combinations_without_repetitions(n:int, k:int):
    return fact(n)/(fact(n-k)*fact(k))

# функция для перестановок без повторений
def perm(n:int):
    return fact(n)
    
# правило произведения  (m + n - 1) * (m + n - 1)
def product(n:int, m:int): 
    otv = (m+n-1)*(m+n-1)
    print ("Всего способов: ",int(otv), '\n')

# Код, реализующий размещение с повторениями
# где n - количество размещений, а k - сколько элементов входит в одно размещение
def placement_with_repetitions(n, k):
    print("Ответ:", n ** k)

# Код, реализующий размещение без повторений
# из n различных жлементов по k элементов
def placement_without_repetitions(n, k):
    print("Ответ:", int(fact(n)/fact(n-k)))

# сочетание с повторениями (n+k-1)!/k!*(n-1)!
def combinations_with_repetitions(n:int, k:int): 
    otv = fact(n+k-1)/(fact(k)*fact(n-1))
    print("Число равновозможных заказов равно: ",int(otv), '\n')

# сочетание без повторений n!/(n-k)!*k!
def combination_without_repetitions_task(n:int, k:int):
    otv = fact(n)/(fact(n-k)*fact(k))
    print("количество способов: ", int(otv), '\n')

# функция, реализующая задачу на перестановки без повторов
def task_on_perm():
    n = int(input("введите n: "))
    print("ответ: ", int(perm(n)))

# функция, реализующая задачу на перестановки с повторениями
def task_on_perm_reps():
    word = input("введите слово: ")
    letters = dict()
    for symb in word:
        letters[symb] = word.count(symb)
    a= []
    for letter in letters:
        a.append(letters[letter])
    print("ответ: ", int(perm_reps(len(word), a)))

# функция, реализующая правило суммы
def task_on_sum():
    a = int(input("введите a: "))
    b = int(input("введите b: "))
    print("ответ: ", int(a+b))

# Главная функция, в которой задаются значения (n, k, m) для использования других функций и тема с помощью choose
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
            print("На подносе лежат a яблок и b груш. Сколькими способами можно взять один фрукт с подноса?") # a=7, b=4, ответ: 11
            task_on_sum()
        
        elif choose == 2:
            print("У вас есть (m) яблок и (n) апельсинов. Сколькими способами можно разместить эти фрукты в ряд так, чтобы каждый фрукт был рядом с другим фруктом?") # в задаче n = 10, m = 5, Ответ: 196
            n = int(input('Введите n: '))
            m = int(input('Введите m: '))
            product(n, m)

        elif choose == 3:
            print("Для создания n-значного пароля используются символы из алфавита {k1,k2,...,k}.") # В условии задачи n = 4, а k = {+,*,A,!,2, 1}. Ответ = 4096
            n = int(input('Введите n: '))
            k = int(input('Введите k: '))
            placement_with_repetitions(n, k)
        
        elif choose == 4:
            print("В хоккейном турнире участвуют n команд. \n"
              "Разыгрываются золотые, серебряные и бронзовые медали. \n"
              "Сколькими способами могут быть распределены медали?") # В условии из учебника в турнире усаствуют 17 команд, k = 3. Ответ = 4080
            n = int(input('Введите n: '))
            k = int(input('Введите k: '))
            placement_without_repetitions(n, k)

        elif choose == 5:
            print("n ребят собрали в саду k яблока. Сколькими способами они могут их разделить между собой?") # в задаче из учебника n = 3, k=63, C=2080
            n = int(input('Введите n: '))
            k = int(input('Введите k: '))
            combinations_with_repetitions(n, k)

        elif choose == 6: 
            print("У вас есть n различных книг, и вы хотите выбрать k книги для чтения. Сколькими способами вы можете выбрать эти книги?") # в задаче n=5, k=3, C=10
            n = int(input('Введите n: '))
            k = int(input('Введите k: '))
            combination_without_repetitions_task(n, k)

        elif choose == 7:
            print("Сколько существует различных перестановок из букв введенного слова?") # в учебнике слово = "уссури" и ответ 180
            task_on_perm_reps()

        elif choose == 8:
            print("Сколькими способами можно расположить на шахматной доске n ладей, чтобы они «не били» друг друга?") # в учебнике при n = 8 ответ 40320
            task_on_perm()

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





