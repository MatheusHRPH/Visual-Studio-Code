'''primeiro = int(input('Primeiro numero:'))
segundo = int(input('Segundo numero:'))
resultado = primeiro+segundo
print('A soma vale {}'.format(resultado))'''

'''Desafio 005
n = int(input('Digite um valor: '))
print('Antecessor = {} \n Sucessor = {}'.format(n-1, n+1))'''

'''Desafio 006
n = int(input("Digite um valor: "))
print('Dobro = {} \nTriplo {} \nRaiz Quadrada = {}'.format(n*2, n*3, n**(1/2)))'''

'''Desafio 007
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
r = float((n1 + n2)/2 )
print('Média = {}'.format(r))'''

'''Desafio 008
n = int(input("Digite um valor: "))
print('{} metros = {} centímetros \n{} metros = {} milímetros'.format(n, n*100 , n, n*1000))'''

'''Desafio 009
n = int(input('Digite um valor: '))
print('{} * {} = {} \n{} * {} = {} \n{} * {} = {} \n{} * {} = {} \n{} * {} = {}'.format(n,1,n*1,n,2,n*2,
n,3,n*3,n,4,n*4,n,5,n*5))
print('{} * {} = {} \n{} * {} = {} \n{} * {} = {} \n{} * {} = {} \n{} * {} = {} \n'.format(n,6,n*6,n,7,n*7,
n,8,n*8,n,9,n*9,n,10,n*10))'''

'''Desafio 010
reais = float(input('Quantos reais você tem?'))
print('Você pode comprar {} dólares '.format(reais/3.27))'''

'''Desafio 011
Largura = float(input('Qual a largura da parede?'))
Altura = float(input('Qual a altura da parede?'))
Area = float(Largura*Altura)
print('A Área da parede é de {}m²'.format(Area))
print('Para pintar a parede você irá gastar {} litros de tinta'.format(Area/2))'''

'''Desafio 012
Preco = float(input('Qual o preço do produto?'))
print('O novo preço com desconto é: {}R$'.format(Preco-Preco*0.05))'''

'''Desafio 013
Salario = float(input('Qual o salário do funcionário?'))
print('Após o aumento o sálario fica {}R$'.format(Salario + (Salario * 0.15)))'''

'''Desafio 014
Celsius = float(input('Qual a temperatura em °C?'))
print('A temperatura em °F é {}'.format(((9 * Celsius) / 5) + 32))'''   

'''Desafio 015
Km = float(input('Quantos Km o carro percorreu?'))
Dia = int(input('Quantos dias o carro foi alugado?'))
print('O valor a pagar é: {}R$'.format((Dia * 60) + (Km * 0.15)))'''

'''Desafio 016
import math
num = float(input('Digite um número '))
print('O número {} tem a parte inteira {}'.format(num, math.trunc(num)))'''

'''Desafio 017
import math
co = int(input('Qual o valor do cateto oposto? '))
ca = int(input('Qual o valor do cateto adjacente? '))
hip = float(math.sqrt(math.pow(co,2) + math.pow(ca,2)))
print('A hipotenusa vale {}'.format(hip))'''

'''Desafio 018 - FAZER!!!
import math
angulo = float(input('Digite o valor do ângulo ')) 
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O ângulo {} tem sen: {:.2f}, cos: {:.2f}, tan: {:.2f}'.format(angulo,sen,cos,tan))'''

'''Desafio 019
import random

a1 = input('Qual o nome do primeiro aluno? ')
a2 = input('Qual o nome do segundo aluno? ')
a3 = input('Qual o nome do terceiro aluno? ')
a4 = input('Qual o nome do quarto aluno? ')
num = random.randint(1, 4)
if num == 1 :
    print('O aluno escolhido foi: {}'.format(a1))
elif num == 2 :
    print('O aluno escolhido foi: {}'.format(a2))
elif num == 3 :
    print('O aluno escolhido foi: {}'.format(a3))
else :
    print('O aluno escolhido foi: {}'.format(a4))'''

'''Desafio 020
import random
n1 = input('Qual o nome do primeiro aluno? ')
n2 = input('Qual o nome do segundo aluno? ')
n3 = input('Qual o nome do terceiro aluno? ')
n4 = input('Qual o nome do quarto aluno? ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)''' 

'''Desafio 021
import pygame
pygame.init()
pygame.mixer.music.load("xaropinho.mp3")
pygame.mixer.music.play()
pygame.event.wait()'''