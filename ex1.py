# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# 6 -> да
# 7 -> да
# 1 -> нет

def is_day_off(day):
    if  (day < 1 or day > 7):
        return 'Неверный день недели'
    if (0 < day < 6):
        return  'Нет'
    if (6<= day < 8):
        return 'Да'



print('Введите день недели', end=' ')

weekDay = int(input())

res = is_day_off(weekDay)

print(f'{weekDay} -> {res}')
