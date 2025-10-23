# Example 1
# request = input('Надеюсь ты изучаешь python? ')
# if request == 'Да, Python.':
#     print('Молодец! Ты хороший!')
#     print('C# хорошо, а Python лучше!')


# Example 2
# course1 = int(input('Дядя, ты сколько лет учился на первом курсе?'))
# course2 = int(input('Дядя, ты сколько лет учился на втором курсе?'))
# course3 = int(input('Дядя, ты сколько лет учился на третьем курсе?'))
# course4 = int(input('Дядя, ты сколько лет учился на четвертом курсе?'))
# if course1 == course2 == course3 == course4:
#     print("Оу! Да ты молодец!")
# else:
#     print("Дядя! Ты не прав!")


# .lower маленкие буквы
# у or and not есть приоритеты: 1 - not 2 - and 3 - or


# Example 3
# age = 17
# with_parents = True
# blacklist = False

# if not blacklist and (age >= 18 or with_parents):
#     print("Доступ разрешен")
# else:
#     print("Досту разрешен")


# Example 4
# is_student = True
# has_card = False
# is_pensioner = False
# blocked = False

# if not blocked and ((is_student and has_card) or is_pensioner):
#     print("Скидка доступна")
# else:
#     print("Скидка не доступна")


# Example 5
# number = int(input("Введите число: "))
# if  9 < number < 100 or -9 < number > -100:
#     print("Число является двузначным")
# else:
#     print("Число является двузначным")


# Example 6
# num = int(input("Ведите трехзначное число: "))

# d3 = num % 10
# d2 = (num // 10) % 10
# d1 = num // 100

# if d1 == d2 or d2 == d3 or d1 == d3:
#     print("Есть одинаковые цифры")
# else:
#     print("Все цифры разные")


# Example 7
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))

# if a > 0 and b > 0 and c > 0:
#     print(3)
# elif (a > 0 and b > 0) or (a > 0 and c > 0) or (b > 0 and c > 0):
#     print(2)
# elif a > 0 or b > 0 or c > 0:
#     print(1)
# else: print(0)


# Example 8
# x = int(input("Введите число: "))
# if x % 2 == 0:
#     print("Четное число")
# else:
#     print("Число нечетное")


# Example 9
# age = int(input("Введите возраст: "))
# if age >= 18:
#     print("Доступ разрешен")
# else: print("Доступ запрешен")


# Example 10
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if a > b:
#     print(a)
# else: print(b)


# Example 11
# x = int(input("Введите координату x: "))
# y = int(input("Введите координату y: "))
# if x > 0 and y > 0:
#     print("Точка во второй четверти")
# elif x < 0 and y > 0:
#     print("Точка во первой четверти")
# elif x > 0 and y < 0:
#     print("Точка во четвертой четверти")
# elif x < 0 and y < 0:
#     print("Точка во третьей четверти")
# else: print("Точка на оси")


# Example 12
# x = int(input("Введите число: "))
# if x % 3 == 0 and x % 5 == 0:
#     print("Делится")
# else: print("Не делится")


# Example 13
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# if (a + b > c) or (a + c > b) or (b + c > a):
#     print("Треугольник существует")
# else: print("Треугольник несуществует")


# Example 14
# x = int(input("Введите год: "))
# if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
#     print("Год високосный")
# else: print("Год не високосный")


# Example 15
# password = input("Введите пароль: ")
# if password == "Python":
#     print("Доступ разрешен")
# else: print("Доступ запрешен")


# Example 16
# x = int(input("Введите число: "))
# if 10 <= x and x <= 20:
#     print(True)
# else: print(False)


# Example 17
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))

# if a > 0 and b > 0 and c > 0:
#     print(3)
# elif (a > 0 and b > 0) or (a > 0 and c > 0) or (b > 0 and c > 0):
#     print(2)
# elif a > 0 or b > 0 or c > 0:
#     print(1)
# else: print(0)


# Example 18
# c = int(input("Введите номер класса: "))
# b = float(input("Введите средний балл: "))
# p = input("Есть ли взыскания(да/нет): ")
# if c >= 9 and b > 4.0 and p == "нет":
#     print(f"Ученик {c} класса допущен к олимпиаде")
# else: print(f"Ученик {c} класса не допущен к олимпиаде")


# Example 19
# age = int(input("Введите возраст: "))
# salary = int(input("Введите зарплату: "))
# deposit = int(input("Введите депозит: "))
# bl = input("Есть ли отметка о не благо надежности (да/нет): ")
# if (21 >= age or age >= 60):
#     print("Возраст не подходит под ограничения")
# elif (salary < 30000 or deposit < 200000):
#     print("Доходы или депозит не достаточны")
# elif (bl == "да"):
#     print("Имеется метка о неблагонадежности")
# else: print("Кредит одобрен")


# Example 20
# ticket = input("Есть билет (да/нет): ")
# time = input("Пришли вовремя (да/нет): ")
# bl = input("В черном списке (да/нет): ")
# if ticket == "нет":
#     print("Нет билета")
# elif time == "нет":
#     print("Вы не вовремя")
# elif bl == "да":
#     print("Вы в черном списке")
# else: print("Посадка разрешена")


# Example 21
# average_point = float(input("Введите средний балл: "))
# project = input("Есть ли проекты(да/нет): ")
# if average_point >= 4.5 or (average_point >= 4.0 and project == "да"):
#     print("Стипендия есть")
# else: print("Стипендии нет")


# Example 22
# login = input("Введите логин: ")
# password = input("Введите пароль")
# if login == "admin" and password == "12345":
#     print("Доступ разрешен")
# elif login == "quest" and password == "":
#     print("Гостевой оступ разрешен")
# else: print("Доступ запрешен")


# Example 23
# debts = input("Есть ли не сданные долги(да/нет): ")
# attendance = int(input("Посещаемость (в процентах): "))
# if debts == "нет" and attendance > 70:
#     print("Студент допущен")
# else: print("Студент не допущен")


#.isdigit()  Проверяет во всей строке есть ли цифры
#any()  Возвращает True, если хотя бы один элемент итерируемого объекта считается «истинным» 


# Example 24
# password = input("Введите пароль: ")
# if len(password) > 6 and (any(ch.isdigit() for ch in password)) and not password == "password":
#     print("Пароль надежный")
# else: print("Пароль не надежный")


# Example 25
# a = int(input("Введите первое число: "))
# b = int(input("Второе первое число: "))
# c = int(input("Третье первое число: "))
# if b - a == c - b:
#     print(f"{a}, {b}, {c} образуют арифметическую прогрессию")
# else: print(f"{a}, {b}, {c} не образуют арифметическую прогрессию")


# Example 26
# age = int(input("Введите возраст: "))
# maintainers = input("Есть ли сопровождающие(да/нет): ")
# tickets = input("Есть билет (да/нет): ")
# if age < 12 and maintainers == "нет":
#     print("Нет сопровождающих")
# elif 18 > age > 12 and tickets == "нет":
#     print("Нужен билет")


# Example 27
# age = int(input("Введите возрвст"))
# employee = input("Сотрудник компании(да/нет): ")
# if age < 18 or age > 65 or employee == "да":
#     print("проезд бесплатный")
# else: print("проезд платный")


# Example 28
# age = int(input("Введите возрвст"))
# debts = input("Есть ли задолжность(да/нет): ")
# tickets =  input("Есть читательский билет (да/нет): ")
# if age > 12 and tickets == "да" and debts == "нет":
#     print("Читатель может взять книгу")
# else: print("Читатель не может взять книгу")


#.strip  Удаляет пробелы


# Example 29
# course = int(input("Введите курс: "))
# average = float(input("Введите средний балл: "))
# contest = input("Есть ли победы в конкурсах (да/нет): ").strip().lower()

# if course >= 3 and (average >= 4.3 or contest == "да"):
#     print("Студент допущен к стажировке")
# else: print("Студент не допущен")


# Example 30
# day = int(input("Введите день: "))
# month = int(input("Введите месяц: "))
# if month < 1 or month > 12:
#     print("Такой даты не существует")
# elif day < 1 or (month in [1,3,5,7,8,10,12] and day > 31) or (month in [4,6,9,11] and day > 30) or (month == 2 and day > 29):
#     print("Такой даты не существует")
# else: print(f"Дата {day}.{month} существует")


# Example 31
