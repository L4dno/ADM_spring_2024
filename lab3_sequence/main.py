#Лабороторная работа №3: Князев Артём, Хапков Михаил, Позоян Рафаэль
class Sequence:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __repr__(self):
        return repr(self.data)

    def shift(self, steps):
        """
        Сдвигает элементы последовательности на заданное количество шагов.
        Если steps > 0, элементы сдвигаются вправо.
        Если steps < 0, элементы сдвигаются влево.
        """
        if steps > 0:
            return Sequence(self.data[-steps:] + self.data[:-steps])
        elif steps < 0:
            return Sequence(self.data[-steps:] + self.data[:-steps])
        else:
            return self

    def shift_left(self, steps=1):
        """
        Сдвигает элементы последовательности влево на заданное количество шагов.
        """
        return self.shift(-steps)

    def shift_right(self, steps=1):
        """
        Сдвигает элементы последовательности вправо на заданное количество шагов.
        """
        return self.shift(steps)

def main():
    user_input = input("Введите массив целых чисел в формате [1, 2, 3, 4, 5]: ")
    
    numbers_str = user_input.strip('[]').split(',')
    
    integer_array = [int(num.strip()) for num in numbers_str]
    seq = Sequence(integer_array)
    print(f'ваш массив: {seq} \n') # Вывод: [1, 2, 3, 4, 5]

    step = int(input("Введите количество шагов, на которое будет осуществляться сдвиг: "))

    seq_shifted_right = seq.shift_right(step)
    print(f'Сдвиг вправо на {step} элемента:')
    print(seq_shifted_right) # Вывод: [4, 5, 1, 2, 3]

    seq_shifted_left = seq.shift_left(step)
    print(f'Сдвиг влево на {step} элемента:')
    print(seq_shifted_left) # Вывод: [3, 4, 5, 1, 2]

if __name__ == '__main__':
    main()