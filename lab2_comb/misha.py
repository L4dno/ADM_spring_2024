# функция считает факториал числа
def fac(n):
    if n<2:
        return 1
    return n * fac(n-1)

# функция для перестановок без повторений
def perm(n):
    return fac(n)

# вычисление перестановок с повторениями
# где a - массив длины n с количеством
# разных элементов
def perm_reps(n, a):
    tmp = 1
    for item in a:
        tmp *= fac(item)
    return int(fac(n)/tmp)


# функция, реализующая задачу на перестановки без повторов
def task_on_perm():
    # в учебнике при n = 8 ответ 40320
    condition = "Сколькими способами можно расположить на шахматной доске n ладей, чтобы они «не били» друг друга?"
    print(condition)
    n = int(input("введите n: "))
    print("ответ: " + str(perm(n)))

# функция, реализующая задачу на перестановки с повторениями
def task_on_perm_reps():
    # в учебнике слово = "уссури" и ответ 180
    condition = "Сколько существует различных перестановок из букв введенного слова?"
    print(condition)
    word = input("введите слово: ")
    letters = dict()
    for symb in word:
        letters[symb] = word.count(symb)
    a= []
    for letter in letters:
        a.append(letters[letter])
    print("ответ: " + str(perm_reps(len(word), a)))

