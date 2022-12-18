#URI 1043 - Triângulo

'''Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X
Entrada

A entrada contém três valores reais.
Saída

O resultado deve ser apresentado com uma casa decimal.'''

valores = list(map(float, input().split()))
a = valores[0]
b = valores[1]
c = valores[2]

if (a + b) > c and (a + c) > b and (b + c) > a:
  print(f'Perimetro = {a + b + c:.1f}')
else:
  print(f'Area = {(a + b) * c / 2}')
  
