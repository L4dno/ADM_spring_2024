'''
Князев Артём - БПМ-22-4 - Практическая работа №6 - вариант №3
'''

# Определение класса Stella
class Stella():
    # Конструктор класса, принимающий список перестановок
    def __init__(self, permutation):
        # Сохранение переданного списка перестановок в атрибут класса
        self.permutation = permutation

    # Метод для выполнения алгоритма Стеллы
    def algorithm(self):
        # Получение длины списка перестановок
        n = len(self.permutation)
        # Инициализация массивов z, p, d нулями
        z = [0] * (n + 2)
        p = [0] * (n + 2)
        d = [0] * (n + 2)

        # Заполнение массивов z, p, d начальными значениями
        for i in range(1, n + 1):
            z[i] = self.permutation[i - 1]
            p[i] = i
            d[i] = -1

        # Дополнительная инициализация для массива d
        d[1] = 0
        # Инициализация переменной m
        m = n + 1
        # Заполнение первых и последних элементов массива z
        z[0] = m
        z[n + 1] = m

        # Инициализация счетчика перестановок
        k = 0

        # Основной цикл алгоритма
        while m != 1:
            k += 1
            # Вывод текущего состояния массива z
            print(f"{' '.join(map(str, z[1:n + 1]))}")

            # Внутренний цикл для обновления m
            m = n
            while z[p[m] + d[m]] > m:
                d[m] = -d[m]
                m -= 1

            # Обновление массивов z и p
            pm = p[m]
            dm = pm + d[m]
            w = z[pm]
            z[pm] = z[dm]
            z[dm] = w

            zpm = z[pm]
            w = p[zpm]
            p[zpm] = pm
            p[m] = w

        return k

# Определение функции main, которая будет выполняться при запуске скрипта
def main():
    # Запрос у пользователя ввода числа n, которое определяет размер перестановки
    n = int(input("Введите размер перестановки: "))
    # Вывод сообщения о начале генерации перестановок для заданного n
    print(f"\nПерестановки размером {n}")
    # Создание списка перестановок от 1 до n
    initial_permutation = list(range(1, n + 1))
    # Создание экземпляра класса
    stella_instance = Stella(initial_permutation)
    # присваиваем результат работы алгоритма в result
    result = stella_instance.algorithm()
    print(f"\nРезультат в виде общего количества перестановок: {result}")

if __name__ == "__main__":
    main()