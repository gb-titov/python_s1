# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

from math import sqrt

def get_user_input_as_int(msg):
    print(msg, end='')
    return int(input())

x1 = get_user_input_as_int('1 точка X: ')
y1 = get_user_input_as_int('1 точка Y: ')
x2 = get_user_input_as_int('2 точка X: ')
y2 = get_user_input_as_int('2 точка Y: ')

distance = round(sqrt(((x2-x1)**2) + ((y2-y1)**2)), 2)

print(f"A ({x1},{y1}); B ({x2},{y2}) -> {distance}")
