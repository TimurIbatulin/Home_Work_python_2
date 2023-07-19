# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

import fractions


first_fraction = str(input('Введите первую дробь в формате "13/57" - '))
second_fraction = str(input('Введите вторую дробь в формате "13/57" - '))

first = first_fraction.split('/')
second = second_fraction.split('/')

denominator = int(first[1]) * int(second[1])
print(first[0], first[1], second[0], second[1])
addition = (int(first[0])*int(second[1])) + (int(second[0]) * int(first[1]))
print(addition)
multiplication = int(first[0]) * int(second[0])
denominator_m = denominator
for i in range(2, 9, 1):
    if denominator % i == 0:
        if addition % i == 0:
            denominator /= i
            addition /= i
    if denominator_m % i == 0:
        if multiplication % i == 0:
            denominator_m /= i
            multiplication /= i

print(first_fraction, ' + ', second_fraction, ' = ', int(addition), '/', int(denominator))
print(first_fraction, ' * ', second_fraction, ' = ', int(multiplication), '/', int(denominator_m))

f1 = fractions.Fraction(int(first[0]), int(first[1]))
f2 = fractions.Fraction(int(second[0]), int(second[1]))
print('Проверка через модуль fraction ', 'Сложение = ', f1+f2, 'Умножение = ', f1+f2)