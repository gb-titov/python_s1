# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def is_true(first, second, third):
    return not(first or second or third) == (not first or not second or not third)

def print_res(predicat):
    res = is_true(predicat[0], predicat[1], predicat[2])
    print(f'{predicat[0]}, {predicat[1]}, {predicat[2]} -> {res}')


print_res([0, 0, 0])
print_res([0, 0, 1])
print_res([0, 1, 0])
print_res([0, 1, 1])
print_res([1, 0, 0])
print_res([1, 0, 1])
print_res([1, 1, 0])
print_res([1, 1, 1])
