#Лабораторная работа №1: Михаил Хапков, Князев Артём, Рафаэль Позоян
#Группа БПМ-22-4

import tkinter as tk
from tkinter import ttk
from math import sqrt

import math

alph = '0123456789ABCDEF'

# функция переводит число в десятичную СС
def to_dec(num: str, radix: int) -> int:

    tmp = 1
    res = 0

    for digit in num[::-1]:
        res += alph.index(digit) * tmp
        tmp *= radix

    return res

# функция переводит число из десятичной в любую
def dec_to_other(num: float, radix: int) -> str:
    num = float(num)
    str_num = str(num)
    fractional_part, whole_part = math.modf(num) # выделяем целую и дробную части числа
    res = 0
    ans = ''

    whole_part = int(whole_part)

    # переводим целую часть числа
    while whole_part >= radix:
        ans += alph[whole_part % radix]
        whole_part //= radix

    ans += alph[whole_part]

    ans = ans[::-1]

    if num.is_integer():
        return ans

    ans += '.'

    # переводим дробную часть
    for i in range(10):
        fractional_part *= radix
        tmp = math.modf(fractional_part)
        ans += alph[int(tmp[1])]
        fractional_part = tmp[0]

    return ans

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Калькулятор")
        # Увеличиваем размер окна калькулятора
        self.master.geometry("1400x500")

        self.number_entry = ttk.Entry(self.master, width=20)
        self.number_entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        # Добавляем параметр font для увеличения размера шрифта кнопок
        button_style = ttk.Style()
        button_style.configure('TButton', font=('Helvetica',  20))

        self.button_1 = ttk.Button(self.master, text="1", command=lambda: self.button_click(1))
        self.button_2 = ttk.Button(self.master, text="2", command=lambda: self.button_click(2))
        self.button_3 = ttk.Button(self.master, text="3", command=lambda: self.button_click(3))
        self.button_4 = ttk.Button(self.master, text="4", command=lambda: self.button_click(4))
        self.button_5 = ttk.Button(self.master, text="5", command=lambda: self.button_click(5))
        self.button_6 = ttk.Button(self.master, text="6", command=lambda: self.button_click(6))
        self.button_7 = ttk.Button(self.master, text="7", command=lambda: self.button_click(7))
        self.button_8 = ttk.Button(self.master, text="8", command=lambda: self.button_click(8))
        self.button_9 = ttk.Button(self.master, text="9", command=lambda: self.button_click(9))
        self.button_0 = ttk.Button(self.master, text="0", command=lambda: self.button_click(0))
        self.button_a = tk.Button(text='A',bd=5,font = ('Arial', 14), command=lambda : self.button_click('A')).grid(row=6, column=0,stick='wens',padx=5,pady=5)
        self.button_b = tk.Button(text='B',bd=5,font = ('Arial', 14), command=lambda : self.button_click('B')).grid(row=6, column=1,stick='wens',padx=5,pady=5)
        self.button_c = tk.Button(text='C',bd=5,font = ('Arial', 14), command=lambda : self.button_click('C')).grid(row=6, column=2,stick='wens',padx=5,pady=5)
        self.button_d = tk.Button(text='D',bd=5,font = ('Arial', 14), command=lambda : self.button_click('D')).grid(row=7, column=0,stick='wens',padx=5,pady=5)
        self.button_e = tk.Button(text='E',bd=5,font = ('Arial', 14), command=lambda : self.button_click('E')).grid(row=7, column=1,stick='wens',padx=5,pady=5)
        self.button_f = tk.Button(text='F',bd=5,font = ('Arial', 14), command=lambda : self.button_click('F')).grid(row=7, column=2,stick='wens',padx=5,pady=5)
        self.button_clear = ttk.Button(self.master, text="C", command=self.button_clear)
        self.button_dot = ttk.Button(self.master, text=".", command=self.button_dot).grid(row=1, column=4, stick='wens',padx=5,pady=5)
        self.button_add = ttk.Button(self.master, text="+", command=self.button_add)
        self.button_equal = ttk.Button(self.master, text="=", command=self.button_equal)
        self.button_subtract = ttk.Button(self.master, text="-", command=self.button_subtract)
        self.button_multiply = ttk.Button(self.master, text="*", command=self.button_multiply)
        self.button_divide = ttk.Button(self.master, text="/", command=self.button_divide)
        self.button_modulus = ttk.Button(self.master, text="%", command=self.button_modulus)
        self.button_sqrt = ttk.Button(self.master, text="√", command=self.button_sqrt)
        self.button_neg = ttk.Button(self.master, text="+/-", command=self.button_neg)
        # Добавление кнопки для изменения системы счисления
        self.button_change_base = ttk.Button(self.master, text="Change Base", command=self.change_base)
        self.button_change_base.grid(row=0, column=6, padx=5, pady=5)

        # Добавление выпадающего списка для выбора системы счисления
        self.add_base_selector()
        
        
        self.button_1.grid(row=1, column=0, stick='wens',padx=5,pady=5)
        self.button_2.grid(row=1, column=1, stick='wens',padx=5,pady=5)
        self.button_3.grid(row=1, column=2, stick='wens',padx=5,pady=5)
        self.button_add.grid(row=1, column=3, stick='wens',padx=5,pady=5)

        self.button_4.grid(row=2, column=0, stick='wens',padx=5,pady=5)
        self.button_5.grid(row=2, column=1, stick='wens',padx=5,pady=5)
        self.button_6.grid(row=2, column=2, stick='wens',padx=5,pady=5)
        self.button_subtract.grid(row=2, column=3, stick='wens',padx=5,pady=5)
        self.button_modulus.grid(row=2, column=4, stick='wens',padx=5,pady=5)

        self.button_7.grid(row=3, column=0, stick='wens',padx=5,pady=5)
        self.button_8.grid(row=3, column=1, stick='wens',padx=5,pady=5)
        self.button_9.grid(row=3, column=2, stick='wens',padx=5,pady=5)
        self.button_multiply.grid(row=3, column=3, stick='wens',padx=5,pady=5)
        self.button_sqrt.grid(row=3, column=4, stick='wens',padx=5,pady=5)

        self.button_clear.grid(row=4, column=0, stick='wens',padx=5,pady=5)
        self.button_0.grid(row=4, column=1, stick='wens',padx=5,pady=5)
        self.button_equal.grid(row=4, column=2, stick='wens',padx=5,pady=5)
        self.button_divide.grid(row=4, column=3, stick='wens',padx=5,pady=5)
        self.button_neg.grid(row=4, column=4, stick='wens',padx=5,pady=5)

        self.f_num = 0.0
        self.math = ""

    def button_subtract(self):
        first_number = self.number_entry.get()
        self.math = "subtraction"
        self.f_num = float(first_number)  # Используем float для поддержки вещественных чисел
        self.number_entry.delete(0, tk.END)

    def button_click(self, number):
        current = self.number_entry.get()
        if number == ".":
            self.button_dot()
        base = int(self.base_selector.get())  # Получить текущую систему счисления
        if base ==  10:
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, str(current) + str(number))
        else:
            # Преобразовать число в выбранную систему счисления
            new_number = dec_to_other(str(current)+str(number), base)
            #float(str(current) + str(number), base)
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, format(new_number, f'0{len(str(new_number))}'))

    def button_clear(self):
        self.number_entry.delete(0, tk.END)

    def button_add(self):
        first_number = self.number_entry.get()
        self.math = "addition"
        self.f_num = float(first_number)
        self.number_entry.delete(0, tk.END)

    def button_equal(self):
        second_number = self.number_entry.get()
        base = float(self.base_selector.get())  # Получить текущую систему счисления
        self.number_entry.delete(0, tk.END)

        # Выполнение операции в десятичной системе счисления
        decimal_result = self.perform_operation(float(self.f_num), float(second_number))

        # Преобразование результата в выбранную систему счисления
        if base !=   10:
            result = format(float(decimal_result), f'0{len(str(float(decimal_result)))}')
        else:
            result = str(decimal_result)

        self.number_entry.insert(0, result)

    def button_subtract(self):
        first_number = self.number_entry.get()
        self.math = "subtraction"
        self.f_num = float(first_number)  # Используем float для поддержки вещественных чисел
        self.number_entry.delete(0, tk.END)

    def perform_operation(self, num1, num2):
        if self.math == "addition":
            return num1 + num2
        elif self.math == "subtraction":  # Добавлено условие для вычитания
            return num1 - num2
        elif self.math == "multiplication":
            return num1 * num2
        elif self.math == "division":
            if num2 ==  0:
                return "Error: Division by zero"
            else:
                return num1 / num2
        elif self.math == "modulus":
            return num1 % num2
        else:
            return "Unknown operation"

    def button_multiply(self):
        first_number = self.number_entry.get()
        self.math = "multiplication"
        self.f_num = float(first_number)
        self.number_entry.delete(0, tk.END)

    def button_dot(self):
        current = self.number_entry.get()
        if "." not in current:  # Проверяем, что в текущем числе еще нет плавающей точки
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, current + ".")

    def button_divide(self):
        first_number = self.number_entry.get()
        self.math = "division"
        self.f_num = float(first_number)
        self.number_entry.delete(0, tk.END)

    def button_modulus(self):
        first_number = self.number_entry.get()
        self.math = "modulus"
        self.f_num = float(first_number)
        self.number_entry.delete(0, tk.END)

    def button_sqrt(self):
        number = float(self.number_entry.get())
        if number >=  0:
            result = sqrt(number)
            if result.is_integer():
                self.number_entry.delete(0, tk.END)
                self.number_entry.insert(0, float(result))
            else:
                self.number_entry.delete(0, tk.END)
                self.number_entry.insert(0, result)
        else:
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, "Error: Negative square root")

    def button_neg(self):
        current = self.number_entry.get()
        if current.startswith("-"):
            current = current[1:]
        else:
            current = "-" + current
        self.number_entry.delete(0, tk.END)
        self.number_entry.insert(0, current)

    def add_base_selector(self):
        bases = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # Список поддерживаемых систем счисления
        self.base_selector = ttk.Combobox(self.master, values=bases, state='readonly')
        self.base_selector.set(10)  # Установить начальную систему счисления (десятичную)
        self.base_selector.grid(row=0, column=5, padx=5, pady=5)
        
    def change_base(self):
        # Переключение между системами счисления
        current_base = float(self.base_selector.get())
        next_base = (current_base %  16) +  1  # Циклический переход между системами счисления
        self.base_selector.set(next_base)


if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------


# import tkinter as tk



# def calculate():
#     global stroka
#     global hour
#     global minute
#     global second
#     value = calc.get()
#     if step.get() =="time":
#         hour = hour + value.split(".")[0]
#         minute = minute + value.split(".")[1]
#         second = second + value.split(".")[2]
#         if hour[-1] in "+-":
#             hour = hour + "0"
#         print(hour)
#         print(minute)
#         print(second)
#         sec = eval(second)
#         if sec < 0:
#             sec += 60
#             min = eval(minute) - 1
#             if min < 0:
#                 min += 60
#                 hr = eval(hour) - 1
#             else:
#                 hr = eval (hour)
#         else:
#             min = eval(minute)
#             if min < 0:
#                 min += 60
#                 hr = eval(hour) - 1
#             else:
#                 hr = eval(hour)
#         otv = str(hr) + "." + str(min) + "." + str(sec)
#         calc.delete(0, tk.END)
#         calc.insert(0, otv)
#     else:
#         syst = int(step.get())
#         chislo = int(value, syst)
#         temp = stroka + str(chislo)
#         stroka = temp
#         print(stroka)
#         index = stroka.find('^')
#         print(index)
#         if index != -1:
#             chislo1 = int(stroka[0:index])
#             chislo2 = int(stroka[index + 1:])
#             calc.delete(0, tk.END)
#             calc.insert(0, chislo1 ** chislo2)
#         else:
#             calc.delete(0, tk.END)
#             calc.insert(0, round(eval(stroka), 2))
#     stroka = ""
#     hour = ""
#     minute = ""
#     second = ""

# def clear():
#     calc.delete(0, tk.END)
#     stroka = ""
#     hour = ""
#     minute = ""
#     second = ""
#     calc.insert(0, '0')

# def add_digit(digit):
#     global stroka
#     global hour
#     global minute
#     global second
#     value = calc.get()
#     if value[0] == '0':
#         value = value[1:]
#     elif value[0] in '+-/*^':
#         if step.get() == "time":
#             hour = hour + value
#             minute = minute + value
#             second = second + value
#             calc.delete(0, tk.END)
#             value = value[:-1]
#             print(hour)
#             print(minute)
#             print(second)
#         else:
#             temp = stroka + value
#             stroka = temp
#             calc.delete(0, tk.END)
#             value = value[:-1]
#             print(stroka)
#     calc.delete(0, tk.END)
#     calc.insert(0,value+digit)

# def add_operation(operation):
#     global stroka
#     global hour
#     global minute
#     global second
#     value = calc.get()
#     print(value)
#     if value[-1] in '+-*/^':
#         value = value[:-1]
#     elif step.get() =="time":
#         hour = hour + value.split(".")[0]
#         minute = minute + value.split(".")[1]
#         second = second + value.split(".")[2]
#         print (hour)
#         print (minute)
#         print (second)
#     else:
#         syst = int(step.get())
#         chislo = int(value, syst)
#         temp = stroka + str(chislo)
#         stroka = temp
#     print (stroka)
#     calc.delete(0, tk.END)
#     calc.insert(0, operation)

# win = tk.Tk()
# win.geometry(f"255x430+100+200")
# win['bg'] = '#ffc6fe'
# win.title('Калькулятор')

# znach = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "time"]
# step = tk.Spinbox(win, values = znach,font = ('Arial', 10), width = 6)
# step.grid(row=1, column=0)
# calc = tk.Entry(win, justify=tk.RIGHT, font = ('Arial', 12), width = 15)
# calc.insert(0,'0')
# calc.grid(row=1, column=1,columnspan=3)



# tk.Button(text='1',bd=5,font = ('Arial', 14), command=lambda : add_digit('1')).grid(row=3, column=0,stick='wens',padx=5,pady=5)
# tk.Button(text='2',bd=5,font = ('Arial', 14), command=lambda : add_digit('2')).grid(row=3, column=1,stick='wens',padx=5,pady=5)
# tk.Button(text='3',bd=5,font = ('Arial', 14), command=lambda : add_digit('3')).grid(row=3, column=2,stick='wens',padx=5,pady=5)
# tk.Button(text='4',bd=5,font = ('Arial', 14), command=lambda : add_digit('4')).grid(row=4, column=0,stick='wens',padx=5,pady=5)
# tk.Button(text='5',bd=5,font = ('Arial', 14), command=lambda : add_digit('5')).grid(row=4, column=1,stick='wens',padx=5,pady=5)
# tk.Button(text='6',bd=5,font = ('Arial', 14), command=lambda : add_digit('6')).grid(row=4, column=2,stick='wens',padx=5,pady=5)
# tk.Button(text='7',bd=5,font = ('Arial', 14), command=lambda : add_digit('7')).grid(row=5, column=0,stick='wens',padx=5,pady=5)
# tk.Button(text='8',bd=5,font = ('Arial', 14), command=lambda : add_digit('8')).grid(row=5, column=1,stick='wens',padx=5,pady=5)
# tk.Button(text='9',bd=5,font = ('Arial', 14), command=lambda : add_digit('9')).grid(row=5, column=2,stick='wens',padx=5,pady=5)
# tk.Button(text='A',bd=5,font = ('Arial', 14), command=lambda : add_digit('A')).grid(row=6, column=0,stick='wens',padx=5,pady=5)
# tk.Button(text='B',bd=5,font = ('Arial', 14), command=lambda : add_digit('B')).grid(row=6, column=1,stick='wens',padx=5,pady=5)
# tk.Button(text='C',bd=5,font = ('Arial', 14), command=lambda : add_digit('C')).grid(row=6, column=2,stick='wens',padx=5,pady=5)
# tk.Button(text='D',bd=5,font = ('Arial', 14), command=lambda : add_digit('D')).grid(row=7, column=0,stick='wens',padx=5,pady=5)
# tk.Button(text='E',bd=5,font = ('Arial', 14), command=lambda : add_digit('E')).grid(row=7, column=1,stick='wens',padx=5,pady=5)
# tk.Button(text='F',bd=5,font = ('Arial', 14), command=lambda : add_digit('F')).grid(row=7, column=2,stick='wens',padx=5,pady=5)
# tk.Button(text='0',bd=5,font = ('Arial', 14), command=lambda : add_digit('0')).grid(row=2, column=0,stick='wens',padx=5,pady=5)

# tk.Button(text='+',bd=5,font = ('Arial', 14), command=lambda : add_operation('+')).grid(row=3, column=3,stick='wens',padx=5,pady=5)
# tk.Button(text='-',bd=5,font = ('Arial', 14), command=lambda : add_operation('-')).grid(row=4, column=3,stick='wens',padx=5,pady=5)
# tk.Button(text='*',bd=5,font = ('Arial', 14), command=lambda : add_operation('*')).grid(row=5, column=3,stick='wens',padx=5,pady=5)
# tk.Button(text='/',bd=5,font = ('Arial', 14), command=lambda : add_operation('/')).grid(row=6, column=3,stick='wens',padx=5,pady=5)
# tk.Button(text='^',bd=5,font = ('Arial', 14), command=lambda : add_operation('^')).grid(row=7, column=3,stick='wens',padx=5,pady=5)

# tk.Button(text='=',bd=5,font = ('Arial', 14), command=calculate).grid(row=2, column=2, stick='wens',padx=5,pady=5)

# tk.Button(text='.',bd=5,font = ('Arial', 14), command=lambda : add_digit('.')).grid(row=2, column=1, stick='wens',padx=5,pady=5)

# tk.Button(text='CE',bd=5,font = ('Arial', 14), command=clear).grid(row=2, column=3,stick='wens',padx=5,pady=5)

# win.grid_columnconfigure(0,minsize=60)
# win.grid_columnconfigure(1,minsize=60)
# win.grid_columnconfigure(2,minsize=60)
# win.grid_columnconfigure(3,minsize=60)

# win.grid_rowconfigure(1,minsize=60)
# win.grid_rowconfigure(2,minsize=60)
# win.grid_rowconfigure(3,minsize=60)
# win.grid_rowconfigure(4,minsize=60)
# win.grid_rowconfigure(5,minsize=60)
# win.grid_rowconfigure(6,minsize=60)
# win.grid_rowconfigure(7,minsize=60)

# win.mainloop()

