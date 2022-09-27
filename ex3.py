# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3
 
def get_plane_num(x, y):
    if (x > 0 and y > 0):
        return 1
    if (x < 0 and y > 0):
        return 2
    if (x < 0 and y < 0):
        return 3
    if (x > 0 and y < 0):
        return 4
    return 'Точка находится на оси'


print('Введите Х:', end=' ')
x = int(input())
print('Введите Y:', end=' ')
y = int(input())

plane = get_plane_num(x, y)

print(f'x={x}; y={y} -> {plane}')
