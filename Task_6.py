# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

WITHDRAWAL_PERCENTAGE = 1.5
WITHDRAWAL_MIN = 30
WITHDRAWAL_MAX = 600
MULTIPLICITY = 50
TAX_THRESHOLD = 5000000
TAX_ON_WEALTH = 10
check = 0

def examination():
    global check
    if check > TAX_THRESHOLD:
        check = check - (check/100*TAX_ON_WEALTH)
    return check

def tax(x):
    tax_money = float(x*0.015)
    if tax_money < 30:
         x = 30
    elif tax_money > 600:
         x = 600
    else:
         x = tax_money
    return x    



while True:
    choice = int(input('Выберите необходимое действие:\n'\
                       '1 - Пополнить лицевой счет\n'\
                       '2 - Снять деньги\n'\
                       '3 - закончить обслуживание и выйти \n'))
    match choice:
        case 1:
            top_up = int(input('Введите вносимую сумму'))
            if top_up % MULTIPLICITY == 0:
                check = examination() + top_up
                print('Баланс лицевого счета', check)
        case 2:
            take_off = int(input('Введите сумму, которую желаете снять - '))
            check = examination()
            print(tax(take_off))
            if take_off > check - tax(take_off):
                print('Недостаточно средств на лицевом счете. \n'\
                      'Доступный остаток: ', check - tax(take_off))
            else:
                check = check - take_off - tax(take_off)
                print('Денежные средства в размере ', take_off, ' выданы, доступный остаток ', check)
        case 3:
            exit()
        case _:
            check = examination()
            print('Баланс лицевого счета', check)
            continue



            



