import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

semanas = list(range(1, 13))
gastos_marketing = [800, 1200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]
visitas_site = [700, 950, 1100, 1400, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100]
vendas = [45, 65, 85, 100, 130, 155, 170, 190, 210, 230, 250, 270]

# Criar gráfico de dispersão (scatter plot) para cada combinação de variáveis
plt.figure(figsize=(10, 5))

plt.scatter(gastos_marketing, vendas, color='green', label="Dados")

# Adicionar linha de regressão
linha_regressao = 17.776 + 0.0427 * gastos_marketing
plt.plot(gastos_marketing, linha_regressao, color='red', label="Linha de Regressão")

# Título e legendas
plt.title("Gasto em Marketing vs. Número de Vendas com Linha de Regressão")
plt.xlabel("Gasto em Marketing (R$)")
plt.ylabel("Número de Vendas")
plt.legend()

# Gráfico 1: Gasto em Marketing vs. Visitas ao Site
# plt.scatter(gastos_marketing, visitas_site, color='blue')
# plt.title("Gasto em Marketing vs. Visitas ao Site")
# plt.xlabel("Gasto em Marketing (R$)")
# plt.ylabel("Visitas ao Site")
# plt.grid(True)


# #Gráfico 2: Gasto em Marketing vs. Número de Vendas
# plt.scatter(gastos_marketing, vendas, color='green')
# plt.title("Gasto em Marketing vs. Número de Vendas")
# plt.xlabel("Gasto em Marketing (R$)")
# plt.ylabel("Número de Vendas")
# plt.grid(True)

# # Gráfico 3: Visitas ao Site vs. Número de Vendas
# plt.scatter(visitas_site, vendas, color='red')
# plt.title("Visitas ao Site vs. Número de Vendas")
# plt.xlabel("Visitas ao Site")
# plt.ylabel("Número de Vendas")
# plt.grid(True)

# Ajustar espaçamento
# plt.tight_layout()

# Exibir os gráficos
plt.show()

# plt.plot(semanas, gastos_marketing, marker='o', label="Gasto em Marketing (R$)")
# plt.plot(semanas, visitas_site, marker='o', label="Visitas ao Site")
# plt.plot(semanas, vendas, marker='o', label="Número de Vendas")

# plt.title("Evolução dos Gastos, Visitas e Vendas ao Longo das Semanas")
# plt.xlabel("Semana")
# plt.ylabel("Valores")
# plt.legend()

# plt.grid(True)
# plt.show()