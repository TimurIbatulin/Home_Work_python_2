# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

letters = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
hexadecimal = ''

user_number = int(input('Введите число, которое нужно представить в 16тиричном виде - '))
control = user_number
while user_number > 0:
    hexadecimal = hexadecimal + letters.get(user_number%16)
    user_number //= 16
hexadecimal = hexadecimal[::-1]
print(hexadecimal, 'Проверка встроенной функцией - ', hex(control))