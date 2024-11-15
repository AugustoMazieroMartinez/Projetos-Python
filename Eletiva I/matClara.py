import matplotlib.pyplot as plt
import numpy as np

paises = {
    'Japan': 500000,
    'France': 400000,
    'Germany': 400000,
    'Australia': 175000,
    'UK': 850000,
    'Mexico': 150000,
    'Hong Kong': 125000
}
paises = [key for key, val in paises.items() for _ in range(val)]
plt.hist(paises, bins=20)
plt.show()