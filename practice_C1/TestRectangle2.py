from Figure import Rectangle, Square

# Далее создаём два прямоугольника
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
square_1 = Square(5)
square_2 = Square(3)

# Вывод площади наших двух прямоугольников
# print(rect_1.get_area_rectangle())
# print(rect_2.get_area_rectangle())

# Вывод площади наших двух квадратов
# print(square_1.get_area_square())
# print(square_2.get_area_square())

figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure, Square):
        print(f"Square's area: {figure.get_area_square()}")
    elif isinstance(figure, Rectangle):
        print(f"Rectangle's area: {figure.get_area_rectangle()}")

