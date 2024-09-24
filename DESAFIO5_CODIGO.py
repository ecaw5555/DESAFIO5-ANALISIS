import numpy as np
import matplotlib.pyplot as plt
AA = np.array([[1.0001, 1.0000],
               [1.0000, 1.0000]])
bb = np.array([2, 2])

solution = np.linalg.solve(AA, bb)
def eq1(x):
    return (2 - 1.0001 * x) / 1.0000  

def eq2(x):
    return (2 - 1.0000 * x) / 1.0000 

x_values = np.linspace(0, 3, 100)


plt.figure()

plt.plot(x_values, eq1(x_values), label='1.0001X + 1.0000Y = 2', color='blue')
plt.plot(x_values, eq2(x_values), label='1.0000X + 1.0000Y = 2', color='orange')

plt.scatter(solution[0], solution[1], color='red', label=f'Solución: {solution}', zorder=5)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico del sistema de ecuaciones')

plt.grid(True)

plt.legend(loc='upper right')

plt.xlim(0, 3)
plt.ylim(0, 3)

plt.axhline(0, color='black', linewidth=0.5, ls='--')  
plt.axvline(0, color='black', linewidth=0.5, ls='--') 
plt.show()

print(f'Solución del sistema: X = {solution[0]}, Y = {solution[1]}')
