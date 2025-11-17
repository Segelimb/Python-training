# Example 1
# print("🎅")


# Example 2
# s = 'абырвалГ'
# print(s[-1] + s[-2] + s[-3] + s[-4] + s[-5] + s[-6] + s[-7] + s[-8])


# Example 3
# p = "Python"

# for i in range(len(p)):
#     print(i, p[i])

# for i in range(-1, -len(p) - 1, -1):
#     print(i, p[i])


# Example 4
# str = "Python"
# print(str[0], str[-1])


# Example 5
# str = input()
# for i in range(0, len(str), 2):
#     print(str[i])


# Example 6
# s = "pythonураудгу"
# part1 = s[0:6]
# part2 = s[6:9]
# part3 = s[9:13]
# print(part1)
# print(part2)
# print(part3)


# Example 7
# s = "pythonураудгу"
# part1 = s[:6]
# part2 = s[6:9]
# part3 = s[9:]
# print(part1)
# print(part2)
# print(part3)


# Example 8
# s = 'abcdefg'
# print(s[:4])


# Example 9
# s = 'information'
# print(s[-3:])

# Example 10
# s = 'abcdef'
# print(s[1:-1])


# Example 11
# s = 'puthonura'
# print(s[:int(len(s)/2)])
# print(s[int(len(s)/2):])


# Example 12
# s = 'abcdefg'
# print(s[::2])


# Example 13
# s = 'pythonураудгу'
# print(s[:-7])
# print(s[-7:-4])
# print(s[-4:])


# Example 14
# s = "pythonураудгу"
# print(s[:6:1])
# print(s[6:9:1])
# print(s[9::1])


# Example 15
# s ="a1b22c333d4" # Создание строки с буквами и цифрами
# count = 0 # Переменная для подсчета цифр

# for i in range(len(s)): # Цикл для перборки символов в строке
#     ch = s[i] # Извлечение символа под индексом i из строки
#     if ch >= '0' and ch <= '9': # Проверка находится ли символ по коду между 0 и 9 (Проверка на число)
#         count += 1 # Если условие выполняется, то увеличить счетчик на 1
# print("Количество цифр:", count) # Вывод итога