import numpy as np
import matplotlib.pyplot as plt
# import statistics as st
# idades = [25, 30, 35, 40, 45]
# media = sum(idades)/len(idades)
# desvio_padrao = st.stdev(idades)
# print('A média das idades é:', media)
# print('O deesvio padrão das idades é:', desvio_padrao)
idades = [18, 18, 18, 18, 19, 9, 19, 20, 20, 20, 21, 21, 21, 22, 22,23, 24, 25, 25, 26, 28]
plt.hist(idades, bins = 6, edgecolor='k')
plt.title('Histograma de Idades')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()
# dados = np.random.normal(0, 1, 100)

# plt.boxplot(dados)
# plt.title('Box plot de Dados de Exemplo')
# plt.ylabel('Valores')
# plt.show()

# x = np.random.normal(0, 1, 100)
# y = 2 * x + np.random.normal(0, 0.5, 100)

# plt.scatter(x, y)
# plt.title('Gráfico de Disperção de Dados de Exemplo')
# plt.xlabel('Variável x')
# plt.ylabel('Variável y')
# plt.show()