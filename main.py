from datetime import time

import time
import numpy as np
import platform
import matplotlib.pyplot as plt

array1 = np.array([1, 2, 3])
print('array1 type:', type(array1))
print('array2 array 형태:', array1.shape)

array2 = np.array([[1, 2, 3], [2, 3, 4]])
print('array2 type:', type(array2))
print('array2 array 형태:', array2.shape)

array3 = np.array([[1, 2, 3]])
print('array3 type:', type(array3))
print('array3 array 형태:', array3.shape)

print('array1: {:0}차원, array2: {:1}차원, array3: {:2}차원'.format(array1.ndim, array2.ndim, array3.ndim))

list1 = [1, 2, 3]
print(type(list1))
array4 = np.array(list1)
print(type(array4))
print(array4, array4.dtype)

print(type(10))
print(type(10.0))
print('내 이릉은' + ' 조영환' + ' 입니다')
print("*" * 10)
n = 10
print('별표를 ' + str(n) + '번 출력합니다')
print("*" * n)

print('둘리가 "호이!" 하고 말했습니다')
multi_line_string = """
파이썬(영어: Python)은 1991년 프로그래머인 
귀도 반 로섬(Guido van Rossum)이 발표한 고급 프로그래밍 언어로,
플랫폼 독립적이며 인터프리터식, 객체지향적, 동적 타이핑(dynamically typed) 
대화형 언어이다. 파이썬이라는 이름은 귀도가 좋아하는 코미디 〈Monty Python's Flying 
Circus〉에서 따온 것이다."""

print(multi_line_string)
print("2022.05.13".replace('.', '-'))
print("2022-05-13".replace('-', ''))
name = 'Rayner'
print('내 이름은 %s 입니다' % '홍길동')
print('나는 %d살입니다' % 50)
print('나는 %10d살입니다' % 50)
print('{2}의 {0} 점수는 {1}점입니다'.format('수학', 100, '철수'))

a = 2
if a % 2 == 0:
    print('짝수')
else:
    print('홀수')


def doubles(x):
    y = x * x
    return y


print(doubles(6))


def sum(a, b, c):
    x = a + b + c
    return x


print(sum(1, 2, 3))


def f(x):
    y = x * 10
    print('y = ', y)
    return y


f(100)

for i in range(10):
    print('*' * i)

for i in range(10):
    print('=' + str(i) + '=')

x = [10, 20, 30]
print(x[1])

b = {'math': 88, 'english': 90, 'history': 100}
print(b)
print(b['english'])
print((b['math'] + b['english']) / 2)

b = list(range(1, 10, 2))
print(b)
b.append(10)
print(b)

a = [90, 85, 95, 80, 90, 100, 85, 75, 85, 80]
print(len(a))

sum = 10
for i in range(len(a)):
    sum = sum + a[i]
average = sum / len(a)
print(average)


class Rectangle(object):

    def __init__(self, h, v):
        self.h = h
        self.v = v

    def area(self):
        return self.h * self.v


r = Rectangle(10, 20)
a = r.area()
print(a)

now_str = str(time.time() * 1000)
split_list = now_str.split('.')
print(split_list[0].strip())

platform.platform()
