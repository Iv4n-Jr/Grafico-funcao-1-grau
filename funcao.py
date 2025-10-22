import numpy as np
import matplotlib.pyplot as plt

# Gerar valores de x
x = np.linspace(-10, 10, 100)

# Lista de coeficientes para múltiplas retas (a, b)
retas = []
num_retas = int(input("Quantas retas você quer plotar? "))

for i in range(num_retas):
    print(f"\nReta {i+1}:")
    a = float(input(f"Digite o valor de 'a' para a reta {i+1}: "))
    b = float(input(f"Digite o valor de 'b' para a reta {i+1}: "))
    retas.append((a, b))

# Cores diferentes para cada reta
cores = ['blue', 'red', 'green', 'purple', 'orange', 'brown', 'pink', 'gray']

# Calcular pontos de interseção
for i in range(len(retas)):
    for j in range(i + 1, len(retas)):
        a1, b1 = retas[i]
        a2, b2 = retas[j]
        
        # Verificar se as retas são paralelas
        if a1 != a2:
            # Calcular ponto de interseção
            x_intersec = (b2 - b1) / (a1 - a2)
            y_intersec = a1 * x_intersec + b1
            
            # Plotar o ponto de interseção
            plt.plot(x_intersec, y_intersec, 'ko', markersize=8)
            plt.annotate(f'({x_intersec:.2f}, {y_intersec:.2f})',
                        (x_intersec, y_intersec),
                        xytext=(10, 10),
                        textcoords='offset points')

# Plotar o gráfico
plt.figure(figsize=(8, 6))

# Plotar cada reta
for i, (a, b) in enumerate(retas):
    y = a * x + b
    cor = cores[i % len(cores)]  # Usa cores diferentes para cada reta
    plt.plot(x, y, label=f'y = {a}x + {b}', color=cor, linewidth=2)

# Adicionar eixos, grade e título
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.title('Retas das Equações de 1º Grau 🤓☝️')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()

# Mostrar o gráfico
plt.show()