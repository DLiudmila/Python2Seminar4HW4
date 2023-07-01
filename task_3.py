# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте все
# операции поступления и снятия средств в список.


# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

def invoice(money):
    print(f'На счету {money} y.e.')

def menuAtm():
    print('--' * 20)
    print(f'Вывести сумму на счете, нажмите: 1')
    print(f'Снять со счета, нажмите: 2')
    print(f'Положить на счет, нажмите: 3')
    print(f'Вывести историю операций: 4')
    print('--' * 20)
    print(f'Для выхода нажмите : 0')
    print('--' * 20)
    return input(' ->> ')
def invoiceOut(money):
    invoice(money)
    while True:
        print(f'Скольео хотите снять со счета? ')
        outmoney = float(input(' ->> '))
        if outmoney > money:
            print(f'{invoice(money)}, введите сумму корректно')
            continue

        if money > rich:
            money = money - money/rich_tax
            operation_list.append(f'Снят налог на богатых {money/rich_tax}')

        if outmoney*bankTax > bankTaxMax:
            tax = bankTaxMax
        elif outmoney*bankTax < bankTaxMin:
            tax = bankTaxMin
        else:
            tax = outmoney*bankTax

        new_money = money - outmoney - tax
        operation_list.append(f'Снято {outmoney} плюс налог за операцию {tax}')
        break
    return new_money
def invoiceIn(money):
    while True:
        new_money = money
        print(f'Сколько хотите положить? (кратно 50) ')
        moneyIn = int(input(' ->> '))
        if moneyIn % 50 != 0:
            print(f'Введите сумму кратиную 50 ')
            continue
        elif moneyIn % 50 == 0:
            new_money += moneyIn
            operation_list.append(f'Внесено {moneyIn}')
            break
    return new_money
def print_history():
    print(operation_list)

# constants
bankTax = 0.015
bankTaxMin = 30
bankTaxMax = 600
bankPercent = 0.03
rich = 5000000
rich_tax = 1.1

#programm
opCount = 1
current_money = 0
operation_list = []
while True:
    button=menuAtm()

    if button == '1':
        invoice(current_money)
    elif button == '2':
        current_money = invoiceOut(current_money)
        opCount += 1
    elif button == '3':
        current_money = invoiceIn(current_money)
        opCount += 1
    elif button == '4': print_history()
    elif button == '0': break
    else: print(f'Непонятно, повторите: ')

    if opCount % 4 == 0:
        current_money = current_money + current_money*bankPercent
        opCount = 1
