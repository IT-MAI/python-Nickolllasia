# Вариант 11 (матрицы) (классы)
import numpy as np

class Matrix:
    def __init__(self,mat):
        self.mat = mat

    def __str__(self):
        return f'{self.mat}'

    def diagonal(self, offset=0):
        return np.diagonal(self.mat, offset)

    def __add__(self, other):
        if not isinstance(other.mat, np.ndarray):
            other = np.array(other)
        return self.mat + other.mat

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