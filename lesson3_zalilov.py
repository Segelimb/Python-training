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