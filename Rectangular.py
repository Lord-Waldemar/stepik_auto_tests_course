def isrectangular(a, b, c):
    # Добавил проверку на 0 и отрицательные стороны при покрытии тестами
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        return True
    else:
        return False


# Позитивные проверки с перемешанными сторонами
assert isrectangular(3, 4, 5) == True
assert isrectangular(3, 5, 4) == True
assert isrectangular(5, 4, 3) == True

# НЕ прямоугольный треугольник
assert isrectangular(3, 3, 3) == False
assert isrectangular(3, 3, 5) == False

# Отрицательная длина стороны
assert isrectangular(-3, -4, -5) == False
assert isrectangular(-3, 4, 5) == False

# Нулевая длина стороны
assert isrectangular(0, 4, 5) == False
assert isrectangular(0, 0, 0) == False

