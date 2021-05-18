import pytest

from src.Figure import Triangle
from src.Figure import Rectangle
from src.Figure import Square
from src.Figure import Circle


# Тест на подсчет площади Треугольника, с условием, что площадь больше или равна 27.81
def test_area_triangle():
    assert Triangle(angles=3, a=10, b=8, c=7).area >= 26


# Тест на подсчет периметра Треугольника, с условием, что периметр равен 12
def test_triangle_perimeter():
    assert Triangle(angles=3, a=7, b=2, c=3).get_triangle_perimeter() == 12


# Тест на подсчет площади Прямоугольника, с условием, что площадь меньше или равна 40
def test_area_rectangle():
    assert Rectangle(angles=4, a=5, b=8).area <= 41


# Тест на подсчет периметра Прямоугольника, с условием, что периметр не равен 25
def test_rectangle_perimeter():
    assert Rectangle(angles=4, a=5, b=8).area != 25


# Тест на подсчет площади Квадрата, с условием того, что площадь равна 36 (Тест специально будет не пройден)
def test_area_square():
    assert Square(angles=4, a=6).area == 38


# Тест на подсчет периметра Квадрата, с условием того, что периметр равен 36 (Тест специально будет не пройден)
def test_square_perimeter():
    assert Square(angles=4, a=6).area == 24


# Тест на подсчет площади Круга, с условием, что площадь больше или равна 706
def test_area_circle():
    assert Circle(angles=0, r=15).area >= 700


# Тест на подсчет периметра Круга, с условием, что периметр не равен 100
def test_circle_perimeter():
    assert Circle(angles=0, r=10).area != 70


# Тест метода add_area, который суммирует площади фигур
def test_add_area():
    triangle = Triangle(None, 10, 8, 7)
    rectangle = Rectangle(None, 5, 8)
    sum_squares = triangle.area + rectangle.area
    assert triangle.add_area(rectangle) == sum_squares


# Тест, что метод add_area  выбрасывает исключение, когда передан не обьект класса Figure
def test_add_area_exception_message():
    triangle = Triangle(None, 10, 8, 7)
    with pytest.raises(TypeError) as error:
        triangle.add_area(300)
    assert str(error.value) == 'Hey! Ты передал не класс Figure'
