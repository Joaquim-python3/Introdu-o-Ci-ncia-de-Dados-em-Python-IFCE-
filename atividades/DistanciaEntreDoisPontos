import numpy as np
import matplotlib.pyplot as plt


# utilização do teorema de pitágoras
def pitagoras(a, b, p):
    dx = a[0] - p[0]
    dy = b[1] - p[1]
    return np.sqrt((dx ** 2 + dy ** 2))


# criando um ponto P
def pontoP(a, b):
    p.append(b[0])
    p.append(a[1])
    return p

#____________________________________________________##
#____________________________________________________##

p = []
#VALORES
a = [5,6]  # valores de x,y respectivos
b = [1, 1]  # valores de x,y respectivos
pontoP(a, b)

#____________________________________________________##
#____________________________________________________##



# configuração do grafico
plt.title('Distância entre dois pontos')  # titulo
plt.grid(True)  # mostrar fundo
plt.plot(10, 10)  # tamanho do grafico


# plotagem

plt.plot([b[0], p[0]],
         [b[1], p[1]],
         marker='o', label = str(abs(b[1] - p[1])))  # x e y de cima pra baixo respectivamente

plt.plot([a[0], b[0]],
         [a[1], b[1]],
         marker='o', label = str('%.2f' % pitagoras(a,b,p)))  # x e y de cima pra baixo respectivamente

plt.plot([a[0], p[0]],
         [a[1], p[1]],
         marker='o',label = str(abs(a[0] - p[0])))  # x e y de cima pra baixo respectivamente

plt.legend() #chamando label de cada reta
# mostrar
plt.show()
