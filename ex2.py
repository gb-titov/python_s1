# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def is_true(first, second, third):
    return not(first or second or third) == (not first or not second or not third)

print(is_true(False, False, False))