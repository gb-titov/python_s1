# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def get_coordinates_by_plane_num(num):
    if num == 1 or num == '1':
        return 'x > 0 и y > 0'
    if num == 2 or num == '2':
        return 'x < 0 и y > 0'
    if num == 3 or num == '3':
        return 'x < 0 и y < 0'
    if num == 4 or num == '4':
        return 'x > 0 и y < 0'
    return 'Четверть не найдена'


print("Введите номер четверти:", end=' ')
plane_num = input()

print(get_coordinates_by_plane_num(plane_num))