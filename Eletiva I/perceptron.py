import numpy as np

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

learning_rate = 0.1
epochs = 10
weights = np.random.rand(2)
bias = np.random.rand(1)

def step_function(sum):
    return 1 if sum >= 0 else 0

for epoch in range(epochs):
    for i in range(len(x)):
        linear_output = np.dot(x[i], weights) + bias
        prediction = step_function(linear_output)
        
        error = y[i] - prediction
        weights += learning_rate * error * x[i]
        bias += learning_rate * error
    
print('testes de classificação')
for X in x:
    linear_output = np.dot(X, weights) + bias
    prediction = step_function(linear_output)
    print(f'Entrada: {X}, Previsão: {prediction}')