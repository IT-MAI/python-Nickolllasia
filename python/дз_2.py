# Вариант 11 (матрицы) (классы)
import numpy as np

# Класс Матрица, которая принимает на вход матрицу из numpy
class Matrix:
    # Инициализируем поля
    def __init__(self,mat):
        self.mat = mat

    # Выводим удобный для пользователя формат матрицы
    def __str__(self):
        return f'{self.mat}'

    # Возвращает элементы на главной или побочной диагонали
    def diagonal(self, offset=0):
        return np.diagonal(self.mat, offset)

    # Складывает матрицы
    def __add__(self, other):
        if not isinstance(other.mat, np.ndarray):
            other = np.array(other)
        return self.mat + other.mat

    # Перемножает матрицы
    def __mul__(self, other):
        if not isinstance(other.mat, np.ndarray):
            other = Matrix(other)
        return np.dot(self.mat, other.mat)

a = np.array([[13,5],[1,3]])
b = np.array([[12,4],[99,1]])


m1 = Matrix(a)
m2 = Matrix(b)
print(m1)
print(m1.diagonal(1))
print(m1+m2)
print(m1*m2)