# Вывод в консоль осуществляется через команду print:
print("Python")


# Создание переменных, они бывают трех типов int, str, and float:
num = 5
s = "Python"
f_num = 5.7
print(type(num), type(s), type(f_num))


# Так же команда print имеет аргументы sep(разделитель между элем.) и end(окончание строки):
print(num, s, f_num, sep = "|", end = " Конец строки \n")


# Существует комманда input для считывания из консоли:
print(input("Введите слово, программа его повторит: "))


# С числовыми переменными можно выполнять арифметические операции (Строковые можно только складывать и умножать):
a = 12
b = 5

sum_ = a + b
defference = a - b 
multiplication = a * b
divide = a / b
integer_division = a // b
reminder = a % b
expanent = a ** b

print(a, '+', b, '=', sum_)
print(a, '-', b, '=', defference)
print(a, '*', b, '=', multiplication)
print(a, '/', b, '=', divide)
print(a, '//', b, '=', integer_division)
print(a, '%', b, '=', reminder)
print(a, '**', b, '=', expanent)

print(s*5 + " Класс")


# Так же есть условные операторы if(если), else(иначе), elif(Иначе если):
if a == 10:
    print(f"a = {a}") #f строкипозволяют использовать переменные в ней указвая их в {}
elif b == 4:
    print(f"b = {b}")
else: print(f"a не равно 10 и b не равно 4")


# Так же можно использовать логические операнды and(И), or(Или), not(Не)
print(not((a == 10 or b == 5) and a == 12))


# Существуют циклы for и while
for i in range(len(s)): #len возвращает длинну списка (строка тоже список, но особенный)
 print(s[i])

i = 0
while(i < len(s)):
 print(s[i].lower()) # метод .lower() делает все буквы строки маленькими
 i += 1


# К элементам списка можно обращаться через срезы([от какого элемента:по какой элемент:с каким шагом]):
print(s[0:-2:2])


# 