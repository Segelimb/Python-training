# Example 1
# for i in range(10):
#     print("Здравствуйте, уважаемый Андрей Павлович!!!")


# Example 2
# print('Ура! У нас C++\n\n')
# print('Ура! У нас C#\n\n')

# for i in range(5):
#     print("Нет! Мы любим только Python!\n\n")


# Example 3
# for i in range(13):           #С нуля нумерация
#     print(i)


# range(start, stop, step)          начало, конец, шаг


# Example 4
# for i in range(5):
#     print(f"{i + 1}. Привет, студент филлиала УдГУ!")


# Example 5
# for i in range(5):
#   print(f"Квадрат числа {i + 1} равен {(i + 1) ** 2 }")


# Example 6
# for i in range(1, 11):
#     if i % 2 == 0:
#         result = "четное число"
#     else: result = "нечетное число"
#     print(i, result, sep = " - ")


# Example 7
# a = 0
# for i in range(1, 6):
#     a = a + i
# print(f"Сумма чисел от 1 до 5 равна {a}")


# Example 8
# for i in range(0, 10):
#     if i < 3 or i > 7:
#         print(f"{i} подходит по условию")


# Example 9
# for i in range(1, 11):
#     print(f"3 × {i} = {3 * i}")


# Example 10
# for i in range(3):
#     age = int(input("Введите возраст: "))
#     if age < 18 or age > 60:
#         print(f"Возраст {age} не подходит для регистрации")
#     else: print(f"Возраст {age} принят")


# Example 11
# for i in range(2, 11):
#     if i % 2 == 0:
#         print(f"{i} - четное")


# Example 12
# for i in range(3):
#     name = input("Введите имя пользователя: ")
#     if name == "admin" or name == "moderator":
#         print(f"Добро пожаловать, {name}!")
#     else: print(f"Пользователь {name} - доступ ограничен")


# Example 13
# for i in range(1, 6):
#      print(f"{i}. Добро пожаловать на занятие по Python!")


# Example 14
# for i in range(1, 6):
#    print(f"Число {i}: квадрат = {i ** 2}, куб = {i ** 3}")


# Example 15
# for i in range(1, 13):
#     if i % 2 == 0 and i % 3 == 0:
#         print(f"{i} - четное и кратно 3")
#     elif i % 2 == 0:
#         print(f"{i} - только четное")
#     elif i % 3 == 0: 
#         print(f"{i} - только кратно 3")


# Example 16
# a = 0
# for i in range(1, 11):
#     if i % 2 != 0:
#         a = a + i
# print(f"Сумма нечетных чисел = {a}")


# Example 17
# for i in range(0, 10):
#     if i <= 3 or i >= 7:
#         print(f"{i} - вне диапозонпа 3-7")


# Example 18
# for i in range(3):
#     age = int(input("Введите возраст: "))
#     if age > 18 and age < 60:
#         print(f"{age} - подходит")
#     elif age < 18:
#         print(f"{age} - слишком молод")
#     elif age > 60:
#         print(f"{age} - пенсионный возраст")


# Example 19
# num = int(input("Введите число: "))
# for i in range(1, 11):
#     print(f"{num} × {i} = {num * i}")


# Example 20
# for i in range(0,51,5):
#     if i % 10 != 0:
#         print(f"{i} - подходит")


# Example 21
# a = 0
# for i in range(1, 5):
#     a = a + (i ** 2)
# print(f"Сумма квадратов = {a}")


# Example 22
# for i in range(3):
#     name = input("Введите имя пользователя: ").strip().lower()
#     if name == "admin":
#         print(f"Доступ разрешен")
#     else: print(f"Пользователь {name} - доступ запрещён")


# Example 23
# num = int(input("Введите N: "))
# a = 0
# for i in range(1, num + 1):
#     a = a + i
# print(f"Сумма чисел от 1 до {num} равна {a}")


# Example 16
# for i in range(10, 0, -1):
#     print(f"Обратный отсчёт:{i}")


# Example 17
# for i in range(1,21):
#     if i > 10 and i % 2 == 0:
#         print(f"{i} - подходит")


# Example 18
# x = int(input("Введите X: "))
# for i in range(1, 11):
#     if i < x:
#         print(f"{i} не больше {x}")
#     else: print(f"{i} больше {x}")


# Example 19
# a = 0
# for i in range(5):
#     num = int(input("Введитте число: "))
#     if num > 0: a = a + num
# print(f"Сумма положительных чисел = {a}")


# Example 20
# for i in range(-5,6):
#     if i >= 0 and i <= 3:
#         print(f"{i} - Нормальная температура")
#     else: print(f"{i} - вне нормы")


# Example 21
# a = 0
# for i in range(4):
#     num = int(input("Введите число: "))
#     if num > 0: a = a + 1
# print(f"Положительных чисел: {a}")


# Example 22
# for i in range(1, 13):
#     if i % 2 == 0 or i % 3 == 0:
#         print(f"{i} - делится на 2 или на 3")


# Example 23
# for i in range(1, 10):
#     if not(i % 2 == 0) and not(i % 3 == 0):
#         print(f"{i} - делится на 2 или на 3")


# Example 24
# word = "Python"
# for i in range(len(word)):
#     print(f"{i + 1}.Буква {word[i]}")


# Example 25
# a = []
# for i in range(5):
#     num = int(input("Введитте число: "))
#     a.append(num)
# print(f"Наибольшее число: {max(a)}")

# num_one = int(input("Введитте число: "))
# for i in range(4):
#     num = int(input("Введитте число: "))
#     if num > num_one:
#         num_one = num
# print(f"Наибольшее число: {num_one}")


# Example 26
n = int(input("Введите число n: "))
# i = 1
# sum = 0
# while i <= n:
#     if i%2 != 0:
#         sum += i
#     i += 1
# print(n)


# Example 27
# n = int(input("Введите число n: "))
# i = 0
# while 2 ** i < n:
#     i += 1
# if 2 ** i == n:
#     print("True")
# else: print("false")


# Example 28
# num = int(input("Введите число (0 - для завершения): "))
# a = 0
# b = 0
# while num != 0:
#     num = int(input("Введите следующее число (0 - для завершения): "))
#     if num > 0:
#         a += 1
#     elif num < 0:
#         b += 1
# print (a,b)


# Example 29
# str = input("Введите число: ")
# i = len(str) - 1
# while i >= 0:
#     print(str[i])
#     i = i - 1


# Example 30
# str = input("Введите число: ")
# i = 0
# while i < len(str):
#     print(str[i])
#     i = i + 1


# Example 31
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# i = max(num1, num2)
# while num1 % i != 0 or num2 % i != 0:
#     i = i - 1
# print(i)


# Example 32
# num = int(input("Введите число: "))
# i = 1
# a = 0
# while i <= num:
#     if num % i:
#         a += 1
#     i += 1
# print(a)


# Example 33
# num = int(input("Введите число: "))
# i = 2
# while i < num:
#     if num % i == 0:
#         print("False")
#         break
#     else: i += 1
# if i == num: print("True")


# Example 34
# n = int(input("Введите число: "))
# original = n
# reversed_num = 0
# while n > 0:
#     digit = n % 10
#     reversed_num = reversed_num * 10 + digit
#     n //= 10
# if reversed_num == original:
#     print(True)
# else:
#     print(False)


# Example 35
# num = 7
# count = 0
# num_p = 0
# while num_p != num:
#     num_p = int(input("Введите число: "))
#     if num_p < num:
#         print("Введеное число меньше")
#     elif num_p > num:
#         print("Введеное число больше")
#     count += 1
# print(count)


# Example 36
# fuel = 50
# expenditure = 3
# km = 0
# while fuel > 0:
#     fuel -= expenditure
#     km += 1
# print(km)


# Example 37
# num = int(input("Введите число: "))
# num_d = num
# d = 1
# while num_d > 9:
#     num_d = num_d // 10
#     d += 1
# rezult = 1
# t = 1
# while num > 9:
#     for i in range(d-1):
#         rezult *= (num // (10 ** (i + 1))) % 10
#     num = rezult
#     rezult = 1
#     print(f"Шаг {t}: {num}")
#     t += 1  
# print(f"Итоговое устойчивое значение: {num}")
# print(f"Количество шагов: {t}")