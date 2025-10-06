# Example 1
# string_example = '2'
# number_example = int(string_example) + 2 * 5
# print(number_example)
# print(string_example)
# print(type(number_example))
# print(type(string_example))


# Example 2
# number1 = -123.45
# number2 = 34.34  
# number3 = int(number1)
# number4 = int(number2)

# print(number3)
# print(number4)


# Example 3
# a = 12
# b = 5

# sum_ = a + b
# defference = a - b 
# multiplication = a * b
# divide = a / b
# integer_division = a // b
# reminder = a % b
# expanent = a ** b

# print(a, '+', b, '=', sum_)
# print(a, '-', b, '=', defference)
# print(a, '*', b, '=', multiplication)
# print(a, '/', b, '=', divide)
# print(a, '//', b, '=', integer_division)
# print(a, '%', b, '=', reminder)
# print(a, '**', b, '=', expanent)


# Example 4
# string1 = 'Люблю Python'
# lenght1 = len(string1) # Считаем длину строки из переменной string1
# lenght2 = len('Сколько тут длина!') # Считаем длину строкового литерала
# print(lenght1)
# print(lenght2) 


# Example 5
# string1 = 'Аб' + 'ыр' + 'валг'
# string2 = 'Аб' + 'ыр' + 'валг'
# string3 = string1 + string2
# string4 = string3 + '!!'
# print(string1)
# print(string2)
# print(string3)
# print(string4)
# print(string4 * 3)


# Example 6


# Homework 1
# a = int(input("Введите делимое (целое): "))
# b = int(input("Введите делитель (целое) : "))
# print("Целая часть (a // b):", a // b) # Получаем целое число от деления (29/6 будет 4 если отбросить остаток)
# print("Остаток (a % b):", a % b) # Получаем остаток от деления (29/6 если отбросить целую часть будет 5)
# print("Проверка: (a//b) * b + (a % b) =", (a//b) * b + (a % b))
# # Получаем число обратно (29/6 при делении на цело получится 4, умножаем на 6 и прибавляем остаток от деления 5 = 29 - начальное число)

# my_float = 0.66666666666
# print(round(my_float, 2))


# Example 7
# a = float(input("Введите дробное число:"))
# print(int(a))


# Example 8
# work = input("Введите слово: ")
# print(work, work, work, work, work)
# print(work * 5)


# Example 9
# name = input("Имя: ")
# lastname = input("Фамилия: ")
# cource = input("Курс: ")

# print("-----")
# print(f"Имя: {name}\nФамилия: {lastname}\nКурс: {cource}") # f строка


# Example 10
# name = input("Введите имя: ")
# print("ваше имя содержит", len(name), "символов")
# print(name * len(name))


# Example 11
# year = input("Введите год: ")
# month = input("Введите месяц: ")
# day = input("Введите день: ")
# print(year, month, day, sep = "-")
# print(year, month, day, sep = "/")
# print(year, month, day, sep = "")


# Example 12
# a = input()
# b = input()
# print("Конкатенация строк: ", a + b)
# print("Числовая сумма: ", int(a) + int(b))


# Example 13
# name = input("Имя: ")
# lang = input("Любимый язык: ")
# year = input("Год начала изучения: ")
# print(name,lang,year, sep = "|")


# Example 14
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# print(min(a, b, c))
# print(max(a, b, c))
# print(abs(min(a, b, c)))


# Example 15
# year = input("Введите год: ")
# month = input("Введите месяц: ")
# day = input("Введите день: ")
# print("Ручная конкатенация: " + day + "." + month + "." + year)
# print("Ручная конкатенация: " + day, month, year, sep = '.')
# print(f"Ручная конкатенация: {day}.{month}.{year}")



#  Homework 2
# name = "* Имя: " + input("Имя: ") + " "
# post = "* Должность: " + input("Должность: ") + " "
# org = "* Организация: " + input("Организация: ") + " "
# if len(name) > len(post):
#     if len(name) > len(org):
#         max_len = len(name)
#     else: max_len = len(org)
# else:
#     if len(post) > len(org):
#         max_len = len(post)
#     else: max_len = len(org)
# print("*" * (max_len + 1))
# print(name.ljust(max_len, " ") + "*")
# print(post.ljust(max_len, " ") + "*")
# print(org.ljust(max_len, " ") + "*")
# print("*" * (max_len + 1))


# Example 16
