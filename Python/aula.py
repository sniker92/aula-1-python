print('Olá Mundo')

# def somar(a, b) :
#     return a + b

# def subtrair(a, b):
#     return a - b

# print(somar(10, 20))
# print(subtrair(30, 10))

import math

def calcular_delta(a,b,c):
    return (b**2) -4*a*c

def calcular_x1(a,b,delta):
    return(-1*b + math.sqrt(delta))/(2*a)

def calcular_x2(a,b,delta):
    return(-1*b - math.sqrt(delta))/(2*a)

a = float(input('Digite o valor de a:'))
b = float(input('Digite o valor de b:'))
c = float(input('Digite o valor de c:'))

delta = calcular_delta(a,b,c)
x1 = calcular_x1(a,b,delta)
x2 = calcular_x2(a,b,delta)

print(delta)
print(x1)
print(x2)




