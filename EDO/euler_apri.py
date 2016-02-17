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

print("")
print("Seja bem vindo ao metodo de euler aprimorado!")
print('Calcularemos a seguinte EDO: dt/dy= 1-t+4y, y(0)=1')
print("")

h = float(input('Digite o tamanho do passo h: ')) #delta x
n = int(input('Digite a quantidade de passos a serem realizados (quantos valores de Yn a serem obtidos): ')) #n passos
print("")

#inicializacao de variaveis
y = 1
t = 0

#loop para realizacao de calculos
for i in range (0, n):

    #funcao especificada no exemplo
    f = 1-t+(4*y)

    #formula de euler aprimorada
    fa = 1-(t+h)+(4*y)+(4*h*f)

    #calculo do yn
    yfinal = ((f+fa)*(h*0.5))

    #incluindo valores nas variaveis para realizar o calculo do proximo yn
    t += h

    #incluindo o y da formula
    yfinal += y

    #mostra o valor do yn calculado
    print ("O valor de y(%d) corresponte a t(%.2f): %.7f") % (i, t, yfinal)

    #y deve assumir o valor do yn calculado
    y = yfinal

    #utilizamos da biblioteca matplotlib para plotar um grafico dos pontos da funcao(tn,yn)
    #assim obtemos uma aproximacao do valor real atraves dos metodos numericos
    plt.show()
    plt.scatter(t, yfinal)
    plt.draw()
    time.sleep(0.25)

#utilizamos da biblioteca time para pararmos o funcionamento do programa para que o grafico seja visivel ate que o CTRL C
#seja pressionado para cancelar a execucao.
time.sleep(10000)
