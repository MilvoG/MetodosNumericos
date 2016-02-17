#Autores: Milvo Gabriel e Lucas Simoes
#Contato: mgprevedello@gmail.com

#Bibliotecas
import matplotlib.pyplot as plt
import pylab
import numpy as np
import time

#utiliza a biblioteca matplotlib para plotar um grafico
#            x      y
plt.axis([0, 1, 0, 70])
plt.ion()

print("")
print("Seja bem vindo ao metodo de runge kutta!")
print('Calcularemos a seguinte EDO: dt/dy= 1-t+4y, y(0)=1')
print("")


h = float(input('Digite o tamanho do passo h: ')) #delta x
n = int(input('Digite a quantidade de passos a serem realizados (quantos valores de Yn a serem obtidos): ')) #n passos
print("")

#inicializacao das variaveis a serem utilizadas no prorama
y = 1
x = 0
k1 = 0 #kn1
k2 = 0 #kn2
k3 = 0 #kn3
k4 = 0 #kn4

yfinal = 0

m = 0 #tn da EDO
t = 0 #T da EDO
o = 0 #yn da EDO

#loop para realizacao de calculos
for i in range (0, n):

    #funcao descrita no programa = k1
    k1 = 1-t+(4*y)

    #utilizar kn1 nesta variavel para calcular k2
    m = t+(0.5*h)

    #utilizar kn1 nesta variavel para calcular k2
    o = y+(0.5*h*k1)

    #calculo de kn2
    k2 = 1-m+(4*o)

    #reseta a variavel para usar novamente pois ela muda para calcular kn3
    o = 0
    o = y+(0.5*h*k2)

    #calculo de kn3
    k3 = 1-m+(4*o)

    #atribui novo valor a variavel t, segundo a formula de runge kutta
    t += h

    #resetando novamente
    o = 0
    o = y+(h*k3)

    #calculo de kn4
    k4 = 1-t+(4*o)

    #pula uma linha
    print("")

    #mostrando valores de k1, k2, k3 e k4 calculados
    print ("Valor de k1 referente y(%d): %.7f") % (i+1, k1)
    print ("Valor de k2 referente y(%d): %.7f") % (i+1, k2)
    print ("Valor de k3 referente y(%d): %.7f") % (i+1, k3)
    print ("Valor de k4 referente y(%d): %.7f") % (i+1, k4)

    #calcula o valor yn+1
    yfinal = (y+(h*(k1+(2*k2)+(2*k3)+k4)/6))

    #Aqui preparamos as variaveis para o proximo passo

    #necessario utilizar o valor de y1 para calcular y2, assim como nos demais metodos
    y = yfinal

    #o valor de t varia, mas precisamos resetar m para nao haver erros no proximo passo, pois t muda ao decorrer dos calculos
    m = 0

    #mostra o valor de yn+1
    print ("Valor de y(%d) correspondente a t(%.2f): %.7f") % (i+1, t, yfinal) #mostra o valor final

    #pular uma linha
    print ("")

    #utilizamos da biblioteca matplotlib funcoes para plotar o grafico
    plt.show()
    plt.scatter(t, yfinal)
    plt.draw()
    time.sleep(0.25)

#utilizamos da biblioteca time uma funcao para nao fechar o grafico ate que pressionemos CTRL C no console
time.sleep(10000)
