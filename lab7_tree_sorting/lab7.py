# Князев Артём, Позоян Рафаэль - БПМ-22-4
# Практическая работа №7

class TreeSorting():
    def __init__(self, input_array): 
        self.input_array = input_array

    def sort_by_floyd(self):
        sorted_array = self.input_array[:]
        position = list(range(len(self.input_array)))
        step = len(self.input_array) // 2
        while step > 0:
            for i in range(step, len(self.input_array)):
                temp = sorted_array[i]
                temp_position = position[i]
                j = i
                while j >= step and sorted_array[j - step] > temp:
                    sorted_array[j] = sorted_array[j - step]
                    position[j] = position[j - step]
                    j -= step
                sorted_array[j] = temp
                position[j] = temp_position
            step //= 2
        return sorted_array

def main():
    arr = [] # пустой массив

    # Создание экземпляра класса
    treesort = TreeSorting(arr)

    continue_ = "yes"
    while continue_ == "yes":
        arr.clear()
        n = int(input('Введите количество элементов массива: '))
        print("Введите значения массива через пробел: ")
        values = input().split() # получаем строку с числами
        for value in values:
            arr.append(int(value)) # преобразуем каждое значение в число и добавляем в массив
        sorted_arr = treesort.sort_by_floyd()
        print("Отсортированный массив: ", sorted_arr)
        continue_ = input("Если хотите продолжить операцию, введите yes, иначе no: ")

if __name__ == '__main__':
    main()
