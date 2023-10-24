import numpy as np
import matplotlib.pyplot as plt

# Condiciones iniciales
x0, y0 = 1, 2
C1, C2 = 1, 1
x1, y1 = 0, 0
C3, C4 = 0, 0
# Solución de la Ecuación lineal de dos variables
def solution(x0, y0, C1, C2, t):
    x = C1 * np.exp(3*t) + C2 * t * np.exp(-3*t)
    y = C1 * np.exp(3*t) + C2 * t * np.exp(-3*t)
    return x, y
def solution(x1, y1, C3, C4, t):
    x = C3 * np.exp(3*t) + C4 * t * np.exp(-3*t)
    y = C3 * np.exp(3*t) + C4 * t * np.exp(-3*t)
    return x, y

# Calcular el valor de x e y para un intervalo de tiempo
t = np.linspace(0, 2, 100)
x, y = solution(x0, y0, C1, C2, t)
x1, y = solution(x1, y1, C3, C4, t)

# Visualizar el resultado en un gráfico
plt.plot(t, x, label='x(t)')
plt.plot(t, y, label='y(t)')
plt.xlabel('t')
plt.ylabel('x and y')
plt.title('Solución de la Ecuación lineal de dos variables')
plt.legend()
plt.show()