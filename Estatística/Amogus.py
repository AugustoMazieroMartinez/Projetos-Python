import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Dados fornecidos
gastos_marketing = np.array([800, 1200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000])
vendas = np.array([45, 65, 85, 100, 130, 155, 170, 190, 210, 230, 250, 270])

# Regressão linear
slope, intercept, r_value, p_value, std_err = stats.linregress(gastos_marketing, vendas)

# Criar gráfico de dispersão
plt.figure(figsize=(8, 6))
plt.scatter(gastos_marketing, vendas, color='green', label="Dados")

# Adicionar linha de regressão
linha_regressao = intercept + slope * gastos_marketing
# plt.plot(gastos_marketing, linha_regressao, color='red', label="Linha de Regressão")

# # Título e legendas
# plt.title("Gasto em Marketing vs. Número de Vendas com Linha de Regressão")
# plt.xlabel("Gasto em Marketing (R$)")
# plt.ylabel("Número de Vendas")
# plt.legend()

# # Exibir o gráfico
# plt.grid(True)
# plt.show()
print(intercept + slope * 8000)