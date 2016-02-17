#Autores: Milvo Gabriel e Lucas Simoes
#Contato: mgprevedello@gmail.com

#Bibliotecas
import matplotlib.pyplot as plt
import pylab
import time

#utiliza a biblioteca matplotlib para plotar um grafico
#            x      y
plt.axis([0, 1, 0, 70])
plt.ion()

#funcao a ser utilizada pelo codigo, esta descrita no livro: Equacoes Diferenciais Elementares e Problemas de Valores de Contorno, BOYCE, E. William

print("")
print("Seja bem vindo ao metodo de euler!")
print('Calcularemos a seguinte EDO: dt/dy= 1-t+4y, y(0)=1')
print("")

#pedimos para que o usuario digite o tamanho do passo (constante) e quantos valores de yn deseja obter
h = float(input('Digite o tamanho do passo h: ')) #delta x
n = int(input('Digite a quantidade de passos a serem realizados (quantos valores de Yn a serem obtidos): ')) #n passos
print("")

#inicializacao de variaveis
y = 1
t = 0

#loop para realizacao de calculos
for i in range (0, n):

    #funcao descrita no programa
    yfinal = y + (h*((1-t)+(4*y)))

    #substitui os valores das variaveis para ser calculado o proximo passo
    y = yfinal
    t += h

    #escreve o resultado do y(i) calculado no console
    print ("Valor de y(%d) correspondente a t(%.2f): %.7f") % (i+1, t, yfinal)

    #utilizamos da biblioteca matplotlib para plotar um grafico dos pontos da funcao(tn,yn)
    #assim obtemos uma aproximacao do valor real atraves dos metodos numericos
    plt.show()
    plt.scatter(t, yfinal)
    plt.draw()
    time.sleep(0.25)

#utilizamos da biblioteca time para pararmos o funcionamento do programa para que o grafico seja visivel ate que o CTRL C
#seja pressionado para cancelar a execucao.
time.sleep(10000)
